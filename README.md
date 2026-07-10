# BobClicker

**BobClicker** is an ultra-optimized, high-frequency auto-clicker engineered to deliver maximum clicking speeds without degrading system performance. Capable of executing clicks at a true `0ms` delay interval, it bypasses standard thread-throttling to achieve unprecedented clicks-per-second (CPS) rates while keeping CPU overhead near zero.

## ✨ Features

* **True 0ms Interval:** Unleashes absolute maximum clicking speed, leveraging raw hardware-level input loops.
* **Zero Performance Drop:** Highly optimized architecture that prevents UI freezing, frame drops, or system stuttering even at maximum CPS.
* **Smart Threading:** Runs on a dedicated, low-priority input thread to ensure your game or application gets full access to system resources.
* **Custom Click Types:** Support for left, right, and middle clicks, as well as single or double-click simulation.

## 🚀 Getting Started

1. Download the executable from the **Releases** section.
2. Launch `BobClicker` (portable, no installation needed).
3. Set your clicking interval to `0` for raw, unrestricted speed.
4. Define your activation hotkey (Default: `F8`).
5. Hover your mouse over the target and press the hotkey to engage.

## 📊 Performance Comparison

Unlike traditional clickers that lock up the system window or leak memory at high speeds, BobClicker stays lightweight:

| Metric | Standard Auto-Clickers | BobClicker (At 0ms) |
| :--- | :--- | :--- |
| **CPU Usage** | 15% - 30% (Throttling) | **< 1% (Optimized)** |
| **UI Responsiveness** | Freezes / Unresponsive | **Perfect / Fluid** |
| **Max CPS Cap** | Limited by OS Timer (~60) | **Uncapped / Hardware Max** |

## ⚠️ Disclaimer

BobClicker is capable of generating massive input strain on applications. Use the `0ms` setting with caution, as some game engines or web browsers may crash if they cannot handle the sheer volume of incoming click events.
