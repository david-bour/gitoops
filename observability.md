# OPENTELEMETRY
- https://opentelemetry.io/
- Observability framework to perform the following for **telemetry data**:
    1. Instrument
    2. Generate
    3. Import
    4. Export

## Problem Statement
I want to change my observability platform in the future (think Splunk to DataDog). How do I do that without heavy lifting? Add a middleman (OTL)

App --- OTL --- DataDog

## Instrumentation
The *code* that records and measure the behavior of an application or piece of infrastructure

__Types of Instrumentation__
- Automatic
    - Think of mutating webhooks that run alongside an application. No code necessary. Similar to DataDog agents.
- Programmatic
    - Think of adding an observability library (dependency) and "manually" configure it by adding labels so the tools can pull behavior data from the application.
- Manual
    - Setting up the observability library AND instrumentation code in the application.