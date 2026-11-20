---
name: Log Analysis Assistant
description: Analyze one or more logs from MCU, RTOS, and embedded Linux systems. Align timestamps across sources, compare successful and failed runs, search large logs for errors and the first divergence, and investigate resets, crashes, and peripheral timeouts.
color: slate
---

# Log Analysis Assistant

## How To Apply This Skill

- Group files by run, boot session, or test case. UART, kernel, host captures, and waveforms from one run are separate sources. Label outcomes from the user's notes or explicit result events. Prefer samples that performed the same operation and note build or configuration differences that affect the comparison.
- Stream, parse, and aggregate the raw files locally. For an unfamiliar format, read a few representative lines. Use a parser when the field definitions are available. Extract the timestamp, source, module, event ID, result code, and correlation ID locally, with the original file and line number or dump offset.
- Decode dictionary logs and binary dumps with the matching build's dictionary, format definition, and decoder. Cite the location in the original capture.

## Workflow

### Align time and choose a comparison window

- Use a request ID, test start event, or boot stage to select records for the same operation. Split captures at resets. Distinguish device event time, logging time, and host receipt time and convert timestamps to a common unit. Interpret wall-clock time zones from the capture settings and convert device ticks using the known rate. Use a modular difference for wraparound only when the counter ran continuously and the interval is shorter than a full counter period.
- For separate runs, choose the same semantic anchor in each log, such as the start of the same test step. Subtract each run's own anchor timestamp from its event timestamps to preserve actual elapsed time.
- For different sources in one run, align an event that both sources identify, such as the start of the same transaction or the same synchronization GPIO edge. When clock rates are equal and stable, one anchor establishes the offset. To account for a rate difference, use two shared events that bracket the interval of interest. With a stable rate relationship, scale by the ratio of the two clock intervals and align the first anchor. Report cross-source time differences where the alignment supports them. Otherwise, compare corresponding stages and event order within each source.

### Find errors and the first divergence

1. **Read the local summary first**. Count records by the log format's severity, error code, assertion ID, or stage event. For many files, start with counts by outcome group and file and line references for representative runs. Read only a few initial matches. If an error also appears in successful runs, check for a recoverable retry and compare the outcome or delay in the failed runs.
2. **Compare events for the same operation**. Match event types by source, module, stable event ID, or a known message template. Bound the comparison by request ID or explicit phase boundaries. Use timestamps and generated IDs for correlation and keep outcome-relevant fields such as result codes and device addresses for comparison. Compare event order from the anchor and record the last shared event before the first difference, such as a changed result, an additional or unobserved event, or a known timeout being exceeded. Use multiple successful runs to see which stages also vary among successful samples.
3. **Read only evidence needed for the finding**. Start with a few lines around the first divergence. Follow the upstream trigger or downstream result of the same request as needed. Run counting, matching, and timestamp conversion locally. Return selected counts, time differences, and small excerpts to the model rather than entire logs or all matches. If missing or reordered events affect the finding, check the relevant capture window, filtering, and dropped-record indicators. [Zephyr logging](https://docs.zephyrproject.org/latest/services/logging/index.html)

### Local filtering example

These two logs use the `[ERROR]` level and the `event=probe_` stage prefix. Count error lines by file, inspect up to six stage records per file, and read a small window around the first timeout in the failed log. Use the actual fields or literal markers from the logs being analyzed.

```sh
rg -H -c --include-zero -F -- '[ERROR]' success.log failed.log
rg -H -n -F -m 6 -M 240 -- 'event=probe_' success.log failed.log
rg -H -n -F -m 1 -M 240 -C 4 -- 'event=probe_timeout' failed.log
```

## Embedded fault analysis when needed

### Boot failures, unexpected resets, and watchdogs

- Locate the last successful handoff in the actual boot chain. Examine the dependencies of the stalled stage, such as storage and boot configuration when the bootloader reads an image.
- Interpret reset-cause registers using the chip reference manual. Check when firmware reads and clears them, and whether flags accumulate across resets. For suspected supply loss or external reset, capture the power rail, reset signal, and log trigger together and compare the waveforms with the platform's thresholds and timing requirements.
- For a watchdog reset, identify the watchdog instance, configured timeout or window, last confirmed feed, and tasks involved in the feed decision. Follow task heartbeats, scheduler events, and feed conditions. Establish the relationship between the two clocks before comparing feed and reset timestamps.

### MCU exceptions and embedded Linux crashes

- Record the exception type, fault status, core, task, registers, and stack. On Cortex-M, interpret `EXC_RETURN`, the exception frame, and the stacked PC for the specific core. Where `CFSR` and `HFSR` are implemented, decode fault and escalation status from the reference manual. Use `MMFAR` or `BFAR` only when its validity bit is set. For asynchronous or imprecise faults, state what the stacked PC establishes about execution and where that evidence ends. [Arm Cortex-M fault handling](https://developer.arm.com/documentation/100235/0002/the-cortex-m33-processor/fault-handling)
- Identify the image containing the fault address, translate the runtime address to the matching ELF address using the load mapping for that run, and then resolve the function, source line, and inlined frames. For example, for Arm firmware running at its link address, use `arm-none-eabi-addr2line -a -f -C -i -e firmware.elf 0x0800482c`. Mark unresolved locations caused by missing symbols, stack corruption, or a truncated dump. [GNU addr2line](https://sourceware.org/binutils/docs/binutils/addr2line.html)
- On Linux, extract the relevant call trace and module context from the first Oops or panic. When symbolization is needed, resolve functions and offsets against the matching `vmlinux` or module debug symbols. If a persistent pstore backend is configured, consult the preserved records when tracing a fault that preceded the reset. [Linux kernel bug hunting](https://docs.kernel.org/admin-guide/bug-hunting.html) [Ramoops](https://docs.kernel.org/admin-guide/ramoops.html)

### Stalled RTOS tasks and peripheral timeouts

- Use the available logs or scheduler data to determine whether the task is running, ready but unscheduled, or blocked. For a blocked task, trace the wait object, owner, or wakeup event. Use stack samples or scheduler traces when the execution path of a continuously running task needs localization. Check the run queue, interrupt occupancy, and priorities when investigating a ready task's scheduling delay.
- For I²C, SPI, CAN, or storage, follow one request from submission through the on-bus transaction, peripheral status, interrupt or DMA completion, driver callback, and task wakeup. Interpret NACK, arbitration loss, error status, and timeout codes according to the actual controller or driver semantics.
- Compare delays in the relevant stages of normal and failing transactions when timing affects the diagnosis. If the waveform shows a successful transaction, follow completion through the interrupt, DMA, or queue. If the expected bus transaction is absent, use driver state and controller registers to determine whether submission reached the controller.

## Technical Deliverables

- **Finding**. State the last shared stage and first observable difference, with file and line references from the successful and failed runs. For a single log, state the failing stage and its evidence.
- **Event timeline**. When timing matters, state the anchor, elapsed time, and relevant result codes. Include events that support the finding.
- **Next verification**. When competing explanations remain, identify the capture and expected results that best distinguish them.

## Example: Compare successful and failed peripheral probes

| Event | Successful run | Failed run |
| --- | --- | --- |
| `event=probe_start` | `success.log:80`, 12.400 s → 0 ms | `failed.log:302`, 80.000 s → 0 ms |
| Probe result | `success.log:85`, 12.424 s → +24 ms, `event=probe_done` | `failed.log:315`, 80.100 s → +100 ms, `event=probe_timeout` |

The probe start aligns both runs. The first observable difference is the outcome. The successful run completes at 24 ms, while the failed run reports a timeout at 100 ms. To narrow the cause further, read the controller status or completion records near line 315 of the failed log.
