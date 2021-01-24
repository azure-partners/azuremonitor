from config import connection_string
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace.tracer import Tracer

tracer = Tracer(
    exporter=AzureExporter(
        connection_string=connection_string),
    sampler=ProbabilitySampler(1.0),
)

def valuePrompt():
    with tracer.span(name="test") as span:
        line = input("Enter a value: ")
        print(line)

def main():
    while True:
        valuePrompt()

if __name__ == "__main__":
    main()
