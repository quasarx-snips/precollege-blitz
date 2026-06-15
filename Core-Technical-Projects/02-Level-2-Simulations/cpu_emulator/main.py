from opcodes import opcodes
def assemble(filename):
    reverse_opcodes = {v: k for k, v in opcodes.items()}
    
    memory = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip().split('#')[0] 
                if not line: continue
                parts = line.split()
                command = parts[0]
                
                if command not in reverse_opcodes:
                    print(f"Error: Unknown instruction '{command}'")
                    return []
                
                opcode_num = reverse_opcodes[command]
                
                if len(parts) > 1:
                    operand = int(parts[1])
                else:
                    operand = 0 
                
                memory.append(opcode_num)
                memory.append(operand)
                
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
        
    return memory

def run_cpu(memory):
    if not memory: return
    pc = 0
    accumulator = 0
    print("--- CPU STARTING ---")

    while True:
        if pc >= len(memory):
            print("Error: Program Counter out of bounds!")
            break

        opcode_num = memory[pc]
        
        if opcode_num not in opcodes:
            print(f"Error: Invalid opcode {opcode_num} at address {pc}")
            break
            
        instruction_name = opcodes[opcode_num]
        operand = memory[pc + 1]
        
        print(f"[PC={pc}] Executing: {instruction_name} {operand}")

        if instruction_name == "HALT":
            print("--- CPU HALTED ---")
            break
            
        elif instruction_name == "JUMP":
            pc = operand
            continue
            
        elif instruction_name == "LOAD":
            accumulator = operand
            print(f"Loaded {operand}. Acc: {accumulator}")
            
        elif instruction_name == "ADD":
            accumulator += operand
            print(f"Added {operand}. Acc: {accumulator}")
            
        elif instruction_name == "SUB":
            accumulator -= operand
            print(f"Subtracted {operand}. Acc: {accumulator}")
            
        elif instruction_name == "STORE":
            print(f"Stored {accumulator} into address {operand}")

        pc += 2 

if __name__ == "__main__":
    program_memory = assemble("test_programs.asm")
    run_cpu(program_memory)