#!/usr/bin/env python3
"""
Chapter 13: Clock Signals
Demonstrates clock signal properties and timing
"""

import time

def calculate_frequency(period):
    """Calculate frequency from period: f = 1/T"""
    return 1.0 / period

def calculate_period(frequency):
    """Calculate period from frequency: T = 1/f"""
    return 1.0 / frequency

def duty_cycle_percentage(high_time, period):
    """Calculate duty cycle as percentage"""
    return (high_time / period) * 100

def display_clock_parameters(frequency):
    """Display all clock signal parameters"""
    period = calculate_period(frequency)
    period_ms = period * 1000
    period_us = period * 1000000
    
    print(f"\nClock Signal Parameters:")
    print(f"  Frequency:    {frequency:,.0f} Hz")
    print(f"  Period:       {period:.9f} seconds")
    print(f"                {period_ms:.6f} milliseconds")
    print(f"                {period_us:.3f} microseconds")
    
    # Assuming 50% duty cycle (square wave)
    high_time = period / 2
    duty = duty_cycle_percentage(high_time, period)
    print(f"  Duty Cycle:   {duty:.1f}% (square wave)")
    print(f"  High Time:    {high_time * 1000:.6f} ms")
    print(f"  Low Time:     {high_time * 1000:.6f} ms")

def visualize_clock_signal(cycles=5, samples_per_cycle=20):
    """Visualize a clock signal"""
    print("\nClock Signal Visualization:")
    print("High: ▄▄▄▄▄▄▄▄▄▄")
    print("Low:  ▁▁▁▁▁▁▁▁▁▁")
    print()
    
    signal = ""
    for cycle in range(cycles):
        # High phase
        signal += "▄▄▄▄▄▄▄▄▄▄"
        # Low phase
        signal += "▁▁▁▁▁▁▁▁▁▁"
    
    print(signal)
    print(f"\n{cycles} complete clock cycles shown")

def simulate_clock_edges(cycles=3):
    """Demonstrate rising and falling edges"""
    print("\nClock Edges:")
    print("Time | State | Edge")
    print("-----|-------|-------------")
    
    time_val = 0
    for cycle in range(cycles):
        print(f" {time_val}   |   0   |")
        time_val += 1
        print(f" {time_val}   |   1   | ↑ Rising Edge")
        time_val += 1
        print(f" {time_val}   |   1   |")
        time_val += 1
        print(f" {time_val}   |   0   | ↓ Falling Edge")
        time_val += 1

def compare_clock_speeds():
    """Compare common clock speeds"""
    clock_speeds = [
        ("Slow clock", 1),
        ("Audio sample rate", 44100),
        ("Old PC (1 MHz)", 1_000_000),
        ("USB 2.0", 480_000_000),
        ("CPU (1 GHz)", 1_000_000_000),
        ("CPU (3.5 GHz)", 3_500_000_000),
    ]
    
    print("\nCommon Clock Frequencies:")
    print("Application           | Frequency       | Period")
    print("----------------------|-----------------|------------------")
    
    for name, freq in clock_speeds:
        period = calculate_period(freq)
        if period >= 1:
            period_str = f"{period:.3f} s"
        elif period >= 0.001:
            period_str = f"{period * 1000:.3f} ms"
        elif period >= 0.000001:
            period_str = f"{period * 1000000:.3f} µs"
        else:
            period_str = f"{period * 1000000000:.3f} ns"
        
        freq_str = f"{freq:,} Hz" if freq < 1000 else f"{freq/1000:,.1f} kHz" if freq < 1_000_000 else f"{freq/1_000_000:,.1f} MHz" if freq < 1_000_000_000 else f"{freq/1_000_000_000:.1f} GHz"
        
        print(f"{name:20s}  | {freq_str:14s} | {period_str}")

def main():
    print("=" * 60)
    print("CHAPTER 13: Clock Signals")
    print("=" * 60)
    
    # Example 1: Clock Signal Basics
    print("\n--- Example 1: Clock Signal Definition ---")
    print("\nA clock signal is a periodic square wave that oscillates")
    print("between two voltage levels (typically 0V and 5V).")
    print("\nKey characteristics:")
    print("  • Periodic: Repeats at regular intervals")
    print("  • Square wave: Sharp transitions")
    print("  • Synchronizes digital circuit operations")
    
    # Example 2: Frequency and Period
    print("\n--- Example 2: Frequency and Period Relationship ---")
    
    # Calculate from period
    period = 0.001  # 1 millisecond
    frequency = calculate_frequency(period)
    print(f"Given period: {period} seconds (1 ms)")
    print(f"Frequency = 1/T = 1/{period} = {frequency} Hz (1 kHz)")
    
    # Calculate from frequency
    print()
    frequency = 1_000_000  # 1 MHz
    period = calculate_period(frequency)
    print(f"Given frequency: {frequency:,} Hz (1 MHz)")
    print(f"Period = 1/f = 1/{frequency:,} = {period:.9f} seconds")
    print(f"                           = {period * 1_000_000:.3f} microseconds")
    
    # Example 3: Clock Parameters
    print("\n--- Example 3: Clock Signal Parameters ---")
    test_frequencies = [1, 1000, 1_000_000, 100_000_000]
    
    for freq in test_frequencies:
        display_clock_parameters(freq)
    
    # Example 4: Visualize Clock
    print("\n--- Example 4: Clock Signal Waveform ---")
    visualize_clock_signal(cycles=5)
    
    # Example 5: Rising and Falling Edges
    print("\n--- Example 5: Clock Edges ---")
    print("\nRising Edge (↑): Transition from LOW (0) to HIGH (1)")
    print("Falling Edge (↓): Transition from HIGH (1) to LOW (0)")
    print("\nDigital circuits often trigger on edges:")
    print("  • Positive edge-triggered: Acts on rising edge")
    print("  • Negative edge-triggered: Acts on falling edge")
    
    simulate_clock_edges(cycles=3)
    
    # Example 6: Duty Cycle
    print("\n--- Example 6: Duty Cycle ---")
    print("\nDuty Cycle = (High Time / Period) × 100%")
    
    period = 1.0  # 1 second for easy calculation
    test_cases = [
        ("Square wave (50%)", 0.5),
        ("25% duty cycle", 0.25),
        ("75% duty cycle", 0.75),
        ("10% duty cycle", 0.1)
    ]
    
    print("\nDuty Cycle Examples (Period = 1 second):")
    print("Description        | High Time | Duty Cycle")
    print("-------------------|-----------|------------")
    
    for description, high_time in test_cases:
        duty = duty_cycle_percentage(high_time, period)
        print(f"{description:18s} | {high_time:8.2f}s | {duty:6.1f}%")
    
    # Example 7: Common Clock Speeds
    print("\n--- Example 7: Common Clock Frequencies ---")
    compare_clock_speeds()
    
    # Example 8: Clock Calculations
    print("\n--- Example 8: Practical Clock Calculations ---")
    
    scenarios = [
        ("CPU at 2.5 GHz", 2_500_000_000),
        ("Arduino (16 MHz)", 16_000_000),
        ("USB 1.0 (12 Mbps)", 12_000_000),
        ("Standard UART (9600 baud)", 9600)
    ]
    
    print("\nScenario              | Frequency    | Period         | Cycles/sec")
    print("----------------------|--------------|----------------|-------------")
    
    for scenario, freq in scenarios:
        period = calculate_period(freq)
        if period >= 0.001:
            period_str = f"{period * 1000:.3f} ms"
        elif period >= 0.000001:
            period_str = f"{period * 1000000:.3f} µs"
        else:
            period_str = f"{period * 1000000000:.3f} ns"
        
        if freq >= 1_000_000_000:
            freq_str = f"{freq / 1_000_000_000:.1f} GHz"
        elif freq >= 1_000_000:
            freq_str = f"{freq / 1_000_000:.0f} MHz"
        elif freq >= 1_000:
            freq_str = f"{freq / 1_000:.1f} kHz"
        else:
            freq_str = f"{freq} Hz"
        
        print(f"{scenario:20s}  | {freq_str:11s} | {period_str:14s} | {freq:,}")
    
    # Example 9: Applications
    print("\n--- Example 9: Clock Signal Applications ---")
    
    applications = [
        "CPU synchronization",
        "Memory timing",
        "Serial communication (UART, SPI, I2C)",
        "USB data transfer",
        "Display refresh (VGA, HDMI)",
        "Analog-to-Digital conversion",
        "Timer/Counter operations",
        "State machine transitions"
    ]
    
    print("\nClock signals are used in:")
    for i, app in enumerate(applications, 1):
        print(f"  {i}. {app}")
    
    print("\n" + "=" * 60)
    print("Key Concepts:")
    print("- Clock signal: Periodic square wave")
    print("- Frequency (f): Cycles per second (Hz)")
    print("- Period (T): Time for one cycle (seconds)")
    print("- Relationship: f = 1/T")
    print("- Rising edge: 0→1 transition")
    print("- Falling edge: 1→0 transition")
    print("- Duty cycle: Percentage of time HIGH")
    print("=" * 60)

if __name__ == "__main__":
    main()
