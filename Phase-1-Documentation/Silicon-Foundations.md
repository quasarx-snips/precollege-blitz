# Silicon Foundations: Building a CPU from Scratch

A minimal 8-bit-inspired CPU emulator and assembler built entirely in Python to demystify how hardware actually executes code.

## 1. Why I Built This
Honestly, I got tired of just writing high-level code without knowing what the hardware is actually doing under the hood. Most people treat Python or C++ like straight-up magic, but let's be real—at the absolute bottom, it’s just a simple loop shuffling numbers around. I wanted to build that loop myself from scratch to see how a CPU actually "thinks."

## 2. The Core Concept: Von Neumann Architecture
I kept things clean and based the emulator on the classic Von Neumann model. No overcomplicated hardware stuff—just three basic Python structures doing all the heavy lifting:
* **Memory:** Literally just a single list (`[]`) holding both the program instructions and the raw data.
* **Program Counter (PC):** An integer acting like a pointer, tracking exactly where we are in memory.
* **Accumulator:** A standard variable to hold the output of whatever calculation just happened.

## 3. The Heartbeat: Fetch-Decode-Execute
The entire CPU is basically just a single `while True` loop running infinitely. Every single clock tick boils down to three straightforward steps:
1. **Fetch:** Grab the next opcode number straight from `memory[pc]`.
2. **Decode:** Use a dictionary (`opcodes.py`) to translate that raw number into something readable like `"LOAD"` or `"ADD"`.
3. **Execute:** Run the operation. If it's a math operation, update the accumulator. If it's a `JUMP`, manually override the PC to point to a completely new spot.

> *"the hardest part wasn't even the math. It was realizing the Program Counter doesn't just move on its own. You have to explicitly code when it should increment and when it needs to sit still."*

---

## 4. The Instruction Set (ISA)
I designed a tiny 6-instruction language for this. To keep parsing simple, every single instruction takes up exactly two slots in memory: one for the command, and one for the data payload.

| Opcode | Name | What it does | Real-world Analogy |
| :--- | :--- | :--- | :--- |
| 1 | LOAD | Puts a number in the accumulator | Picking up a book |
| 2 | STORE | Saves the accumulator value to memory | Putting the book on a shelf |
| 3 | ADD | Adds a value to the accumulator | Adding pages to a stack |
| 4 | SUB | Subtracts a value from the accumulator | Tearing pages out |
| 5 | JUMP | Teleports the PC to a new line | Skipping straight to a specific chapter |
| 6 | HALT | Kills the loop and stops everything | Closing the book entirely |

---

## 5. The Assembler: From English to Binary
Writing raw bytecode like `[1, 5, 3, 2]` by hand is an absolute nightmare and impossible to debug. So, I built a quick assembler script to parse a basic `.asm` file for me.
* It uses a **reverse dictionary** to flip the text commands back into raw numbers.
* It handles **alignment automatically**. Commands like `HALT` don't actually need data, but since the CPU strictly expects two slots per instruction, the assembler automatically pads it with a `0` so the structure doesn't break.

## 6. What’s Next?
Right now, the CPU is pretty basic—it can only handle straight loops and linear math. The next immediate step is adding conditional jumps like `JZ` (Jump if Zero) so it can finally execute actual logic and handle `if/else` statements.
