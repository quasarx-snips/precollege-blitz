## Encryption & Decryption Workflow

```mermaid
graph TD
    subgraph Encryption Process
        A[Start: Plaintext] --> B[Generate Random XOR Key: 0-1023]
        B --> C[Convert Key to 10-bit Binary]
        C --> D[For each character in Plaintext]
        D --> E[XOR char ASCII with XOR Key]
        E --> F[Pad to 3 digits: zfill 3]
        F --> G[Combine all Cipher Blocks]
        G --> H[Append 10-bit Binary Key to payload]
        H --> I[Add Random Noise: insert random lowercase letters]
        I --> J[Return Encrypted Stream]
    end

    subgraph Decryption Process
        K[Start: Encrypted Stream] --> L[Filter Stream: keep digits only]
        L --> M[Extract Last 10 Digits]
        M --> N[Convert 10 digits to Binary Key]
        N --> O[Extract Message Data: all except last 10 digits]
        O --> P[Split Message Data into 3-digit blocks]
        P --> Q[XOR each block with XOR Key]
        Q --> R[Convert back to Characters]
        R --> S[Return Decrypted Plaintext]
    end

    J -.-> K
