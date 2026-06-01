# Base-X Two-Way Conversion Engine 

A high-performance, dependency-free Python implementation of a bidirectional number system converter. This system bypasses standard built-in functions (like `bin()`, `hex()`, etc.) to execute pure algorithmic radix conversions up to Base-36 using continuous division and positional expansion matrices.

Developed as part of the **Precollege_Blitz**.

---

## Features
* **Decimal to Custom Base (`dec_custom`):** Converts any standard Base-10 integer into a user-defined Base-N (from Base-2 up to Base-36) using dynamic remainder mapping loops.
* **Custom Base to Decimal (`custom_dec`):** Decodes custom alphanumeric string representations back into standard Base-10 using positional exponent tracking ($Base^{power-1}$).
* **Case-Insensitive Edge Handling:** Automatically normalizes lowercase and uppercase alphanumeric inputs (e.g., treats `1d` and `1D` identically).

---

##  Algorithmic Architecture

The core mechanics of the bidirectional pipeline are mapped below via Mermaid.js:

```mermaid
flowchart TD
    Start([Start Execution]) --> Choice{Select Operation}
    
    %% Decimal to Custom Path
    Choice -->|dec_custom| DecInput[Input: Base-10 Integer & Target Base]
    DecInput --> Loop1{Is Number > 0?}
    Loop1 -->|Yes| Calc1[Compute: Remainder = Number % Base]
    Calc1 --> Map1[Map Remainder to Char Set]
    Map1 --> Div1[Update: Number = Number // Base]
    Div1 --> Loop1
    Loop1 -->|No| Rev1[Reverse Remainder List]
    Rev1 --> Out1([Return Joined String])

    %% Custom to Decimal Path
    Choice -->|custom_dec| CustInput[Input: Alphanumeric String & Current Base]
    CustInput --> Track[Initialize: Total = 0, Power = Length of String]
    Track --> Loop2{For each Character in String}
    Loop2 -->|Process| Normalize[Normalize to Uppercase]
    Normalize --> Index[Find Character Value in Character Set Matrix]
    Index --> Math[Total += Value * Base ^ Power - 1]
    Math --> DecPower[Decrement Power by 1]
    DecPower --> Loop2
    Loop2 -->|End of String| Out2([Return Total Value])
