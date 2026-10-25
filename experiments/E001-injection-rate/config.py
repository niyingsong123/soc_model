"""E001: vary only the offered read rate against a SimpleMemory.

Run with the registered gem5 executable, not the host Python interpreter.
This configuration has been prepared but has not yet been run with gem5.
"""

import argparse
import json
from pathlib import Path

import m5
from gem5.components.boards.test_board import TestBoard
from gem5.components.memory.simple import SingleChannelSimpleMemory
from gem5.components.processors.linear_generator import LinearGenerator
from gem5.simulate.simulator import Simulator


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    "--rate",
    required=True,
    choices=("0.25GiB/s", "0.5GiB/s", "1GiB/s", "2GiB/s"),
    help="Offered read rate; all other experiment settings remain fixed.",
)
args = parser.parse_args()

memory = SingleChannelSimpleMemory(
    latency="30ns", latency_var="0ns", bandwidth="1GiB/s", size="64MiB"
)
generator = LinearGenerator(
    num_cores=1,
    duration="1ms",
    rate=args.rate,
    block_size=64,
    min_addr=0,
    max_addr=memory.get_size(),
    rd_perc=100,
    data_limit=0,
)

# These parameters are on the underlying PyTrafficGen in the fixed baseline.
# Zero means unlimited here; outstanding will be a separate experiment.
traffic = generator.get_cores()[0].generator
traffic.max_outstanding_reqs = 0
traffic.elastic_req = False

board = TestBoard(
    clk_freq="1GHz",
    generator=generator,
    memory=memory,
    cache_hierarchy=None,
)
simulator = Simulator(board=board)

outdir = Path(m5.options.outdir)
outdir.mkdir(parents=True, exist_ok=True)
with (outdir / "experiment-input.json").open("x", encoding="utf-8") as stream:
    json.dump(
        {
            "experiment": "E001-injection-rate",
            "offered_rate": args.rate,
            "generator_duration": "1ms",
            "block_size_bytes": 64,
            "memory_size": "64MiB",
            "memory_latency": "30ns",
            "memory_latency_var": "0ns",
            "memory_bandwidth": "1GiB/s",
            "read_percentage": 100,
            "max_outstanding_reqs": 0,
            "elastic_req": False,
            "measurement": "start to actual generator exit; no stats reset",
            "drain_at_exit": False,
        },
        stream,
        indent=2,
    )
    stream.write("\n")

simulator.run()
print(
    f"E001 stopped at tick {m5.curTick()} because "
    f"{simulator.get_last_exit_event_cause()}"
)
