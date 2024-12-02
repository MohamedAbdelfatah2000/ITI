verilog_keywords = [
    "module", "endmodule", 
    "wire", "reg", "logic", "bit", "int", "integer", "real", "time", 
    "supply0", "supply1", "tri", "tri0", "tri1", "triand", "trior", "trireg", 
    "input", "output", "inout", 
    "and", "or", "xor", "xnor", "not", "nand", "nor", 
    "always", "initial", "begin", "end", "if", "else", "case", "casex", "casez", 
    "for", "while", "repeat", "forever", 
    "assign", "deassign", "force", "release", 
    "#", "posedge", "negedge", "wait", "disable", 
    "always_comb", "always_ff", "always_latch", 
    "function", "endfunction", "task", "endtask", "return", 
    "parameter", "localparam", "defparam", 
    "define", "ifdef", "ifndef", "else", "endif", "include", 
    "timescale", "celldefine", "endcelldefine", "default_nettype", 
    "unconnected_drive", "no_unconnected_drive", "resetall", 
    "generate", "endgenerate", "genvar", "default", 
    "specify", "endspecify", "event", "fork", "join", "join_any", "join_none", 
    "attribute", "forever", "disable", "priority", "unique", 
    "$display", "$finish", "$stop", "$monitor", "$time", "$random"
]


# This function, only_integer, prompts the user to input a positive integer value.
# The input is validated to ensure it is:
# 1. An integer.
# 2. Positive (greater than 0).
# If the input is invalid, it provides an appropriate error message and prompts the user again.
# If valid, it returns the positive integer.
def only_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("The value must be a positive integer. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
        else:
            return value


# This function, valid_signal_width, prompts the user to input the width of a given signal.
# It uses the only_integer function to ensure the input is:
# 1. A positive integer.
# 2. Valid for specifying the width of a signal.
# The function takes the signal name as a parameter and includes it in the prompt message.
# Returns the validated positive integer representing the signal width.
def valid_signal_width(signal_name):
    return only_integer(f"Enter the width of '{signal_name}' (positive integer): ")



# This function, valid_module_name, continuously prompts the user to enter a valid module name. 
# It checks the input against the following rules:
# 1. The name cannot be empty.
# 2. The name cannot start with a number.
# 3. The name can only contain letters, digits, and underscores.
# 4. The name cannot be a reserved keyword in Verilog (stored in the verilog_keywords list).
# If the input passes all checks, it returns the valid module name.
def valid_module_name():
    while True:
        name = (input("Please enter a valid module name: ").strip()).lower()

        if not name:
            print("Module name cannot be empty, try again.")
        elif name[0].isdigit():
            print("Module name cannot start with a number, try again.")
        elif not name.replace("_", "").isalnum():
            print("Module name can only contain letters, digits, and underscores, try again.")
        elif name in verilog_keywords:
            print(f"'{name}' is a reserved keyword in Verilog, try again.")
        else:
            print(f"Module name '{name}' is valid.")
            return name
    



# This function, valid_unique_variable_name, ensures the user provides a valid and unique variable name.
# It performs the following validations:
# 1. The name cannot be empty.
# 2. The name cannot start with a digit.
# 3. The name must only contain letters, digits, or underscores.
# 4. The name cannot be a reserved keyword in Verilog.
# 5. The name cannot match the module name (case-insensitive).
# 6. The name must not already exist in the provided set of used names.
# If the name passes validation, it prompts the user for the signal width using the valid_signal_width function.
# Adds the validated name to the set of used names and returns the name and its width as a tuple.
def valid_unique_variable_name(moduleName, used_names):
    while True:
        name = (input("Please enter a valid and unique variable name: ").strip()).lower()

        if not name:
            print("Variable name cannot be empty, try again.")
        elif name[0].isdigit():
            print("Variable name cannot start with a number, try again.")
        elif not name.replace("_", "").isalnum():
            print("Variable name can only contain letters, digits, and underscores, try again.")
        elif name in verilog_keywords:
            print(f"'{name}' is a reserved keyword in Verilog, try again.")
        elif name == moduleName.lower():
            print(f"Variable '{name}' can't be the same as the module name, try again.")
        elif name in used_names:
            print(f"Variable '{name}' has already been used, please choose a different name.")
        else:
            print(f"Variable name '{name}' is valid and unique.")
            width = valid_signal_width(name)
            used_names.add(name)
            return name, width



# This function, valid_design_type, prompts the user to specify the type of design 
# as either "synchronous" or "asynchronous". It validates the input based on the following rules:
# 1. The input must be either "synchronous" or "asynchronous" (case-insensitive).
# 2. If the input is invalid, the user is prompted to re-enter the value.
# The function returns the valid design type as a string.

def valid_design_type():
    while True:
        design_type = input("Is the design synchronous or asynchronous? (s/a): ").strip().lower()
        if design_type in ["s", "a"]:
            return design_type
        else:
            print("Invalid input. Please enter 's' for synchronous or 'a' for asynchronous.")




# This function, generate_sequential_logic, generates a basic Verilog template for a sequential logic block. 
# The generated code structure depends on the design type (synchronous or asynchronous) and includes:
# 1. A synchronous block triggered by the clock's rising edge if the design type is "synchronous".
# 2. An asynchronous block triggered by the clock or reset's rising edge if the design type is "asynchronous".
# 3. Placeholders for:
#    - Reset logic inside the `if` condition when the reset signal is active.
#    - Main logic when the reset signal is inactive.
# The function returns the Verilog code template as a formatted string.

def generate_sequential_logic(design_type, clk, reset):
    if design_type == "s":
        return f"""    always @(posedge {clk}) begin
        if (!{reset}) begin
              //-------- Synchronous Reset logic -----------
        end else begin
             //--------- Main logic no Reset -----------
        end
    end
"""
    elif design_type == "a":
        return f"""    always @(posedge {clk} or negedge {reset}) begin
        if (!{reset}) begin
             //------------ Asynchronous reset logic -----------
        end else begin
            //--------------- Main logic no Reset ----------
        end
    end
"""



# This function generates a Verilog combinational logic statement.
# - output_signal: The name of the output signal.
# - inputs: A list of input signal names.
# It combines the inputs using an AND operation and assigns the result to the output signal.

def generate_combinational_logic(output_signal, inputs):
    input_expression = " & ".join(inputs)  
    return f"""
            {output_signal} = {input_expression};  // Combinational logic, Ex: AND all inputs
    """


# This function, generate_verilog_template, creates a full Verilog module template.
# It accepts the module name, lists of input and output signals (with their bit widths),
# a design type (synchronous or asynchronous), and optional clock and reset signal names.
# The function does the following:
# 1. Constructs the module header with parameter declarations for signal widths.
# 2. Declares the module ports, specifying bit-widths for inputs and outputs.
# 3. Generates the sequential logic block based on the provided design type.
# 4. Creates combinational logic for each output, linking it to the input signals.
# 5. Assembles the header, sequential logic, combinational logic, and footer into a complete Verilog module.
# The resulting module includes all the necessary declarations and logic structure for simulation and synthesis.

def generate_verilog_template(moduleName, listofinputs, listofoutputs, design_type, clk="clk", reset="reset"):

    
    module_header = f"module {moduleName} #(\n"

    parameter_list = [f"    parameter {inp.upper()}_WIDTH = {width}," for inp, width in listofinputs]
    parameter_list += [f"    parameter {outp.upper()}_WIDTH = {width}," for outp, width in listofoutputs]


    module_ports = [f"    input  wire {clk},            // Clock input",
                    f"    input  wire {reset},          // Synchronous or asynchronous reset"]
    
    for inp , _  in listofinputs:
        module_ports.append(f"    input  wire [{inp.upper()}_WIDTH-1:0] {inp}, ")

    for outp , _  in listofoutputs:
        module_ports.append(f"    output reg  [{outp.upper()}_WIDTH-1:0] {outp},")

    module_header += "\n".join(parameter_list).rstrip(",") + "\n) (\n"
    module_header +=  "\n".join(module_ports).rstrip(",") + "\n);\n\n"

    
    ############################## Sequential logic #################################
    sequential_logic = generate_sequential_logic(design_type, clk, reset)

    ############################## Combinational logic ##############################
    combinational_logic = "\n".join([generate_combinational_logic(out[0], [inp[0] for inp in listofinputs]) 
                                     for out in listofoutputs])

    ############################## Combine sections #################################
    module_body = (
        "\n\n    // Sequential logic\n" +
        sequential_logic +
        "\n    // Combinational logic\n    always @(*) begin \n " + 
        combinational_logic + "\n    end\n"
        "\n"
    )

    module_footer = f"endmodule // {moduleName}\n"

    return module_header  + module_body + module_footer




# This function, generate_testbench_template, creates a Verilog testbench template for a given module.
# It automates the generation of key components required to simulate and verify the module.
#
# Function Arguments:
# - module_name: Name of the module to test.
# - list_of_inputs: List of input signals for the module, with their names and widths.
# - list_of_outputs: List of output signals for the module, with their names and widths.
# - clk_period: Clock period in nanoseconds for the testbench clock.
# - clk: Name of the clock signal (default is "clk").
# - reset: Name of the reset signal (default is "reset").
#
# Key Features:
# 1. **Testbench Header**:
#    - Adds a `timescale` directive and declares the testbench module.
# 2. **Parameter Declarations**:
#    - Defines local parameters for input and output signal widths, suffixed with `_WIDTH_TB`.
# 3. **Signal Declarations**:
#    - Declares `reg` and `wire` signals corresponding to the module's inputs and outputs.
# 4. **DUT Instantiation**:
#    - Instantiates the design under test (DUT) with parameterized widths and connects testbench signals to DUT ports.
# 5. **Clock Generation**:
#    - Creates a clock signal toggling at half the specified clock period.
# 6. **Stimulus Generation**:
#    - Initializes signals and applies test vectors, including a reset sequence and example test cases.
# 7. **Simulation Control**:
#    - Includes `$finish` to end the simulation after test cases are completed.
#
# The function returns the complete Verilog testbench as a string.

def generate_testbench_template(module_name, list_of_inputs, list_of_outputs, clk_period, clk="clk", reset="reset"):

    
    tb_header = "`timescale 1ns / 1ps\n\n"
    tb_header += f"module {module_name}_TB;\n\n"

    parameters = "    // Parameters\n"
    parameters += f"    localparam CLK_PERIOD = {clk_period};  // Clock period in nanoseconds\n\n"

    parameter_list = [f"    localparam {inp.upper()}_WIDTH_TB = {width};" for inp, width in listofinputs]
    parameter_list += [f"    localparam {outp.upper()}_WIDTH_TB = {width};" for outp, width in listofoutputs]

    parameters += "\n".join(parameter_list)


    signals = "\n    // Testbench signals\n"
    signals += f"    reg {clk}_TB;\n"
    signals += f"    reg {reset}_TB;\n"
    for inp, _ in list_of_inputs:
        signals += f"    reg [{inp.upper()}_WIDTH_TB-1:0] {inp}_TB;\n"
    for outp, _ in list_of_outputs:
        signals += f"    wire [{outp.upper()}_WIDTH_TB-1:0] {outp}_TB;\n"
    signals += "\n"

    ############################## Instantiate DUT ####################################
    dut_instantiation = "    // Instantiate the DUT (Design Under Test)\n"
    dut_instantiation += f"    {module_name} # (\n"
    for inp, _ in list_of_inputs:
        dut_instantiation += f"        .{inp.upper()}_WIDTH({inp.upper()}_WIDTH_TB),\n"
    for outp, _ in list_of_outputs:
        dut_instantiation += f"        .{outp.upper()}_WIDTH({outp.upper()}_WIDTH_TB),\n"
    
    dut_instantiation = dut_instantiation.rstrip(",\n") + "\n    ) DUT (\n\n"

    dut_instantiation += f"        .{clk}({clk}_TB),\n"
    dut_instantiation += f"        .{reset}({reset}_TB),\n"
    for inp, _ in list_of_inputs:
        dut_instantiation += f"        .{inp}({inp}_TB),\n"
    for outp, _ in list_of_outputs:
        dut_instantiation += f"        .{outp}({outp}_TB),\n"
    dut_instantiation = dut_instantiation.rstrip(",\n") + "\n    );\n\n"

    ############################### Clock generation ##################################
    clock_gen = "    // Clock generation\n"
    clock_gen += f"    initial begin\n"
    clock_gen += f"        {clk}_TB = 0;\n"
    clock_gen += f"        forever #(CLK_PERIOD / 2) {clk}_TB = ~{clk}_TB;\n"
    clock_gen += f"    end\n\n"

    ############################### Stimulus generation ################################
    stimulus = "    // Stimulus generation\n"
    stimulus += f"    initial begin\n"
    stimulus += f"        // Initialize signals\n"
    stimulus += f"\n        // Reset sequence\n"
    stimulus += f"        {reset}_TB = 1;\n"
    for inp, _ in list_of_inputs:
        stimulus += f"        {inp}_TB = 0;\n"
    stimulus += f"\n        // Reset sequence end\n"
    stimulus += f"        #20 {reset}_TB = 0;\n\n"

    stimulus += f"        // Test Case 1\n"
    for i, (inp, _ ) in enumerate(list_of_inputs):
        stimulus += f"        #10 {inp}_TB = 1; //input number {i+1}\n"

    stimulus += f"\n        // Test Case 2\n"
    for i, (inp, _ ) in enumerate(list_of_inputs):
        stimulus += f"        ##10 {inp}_TB = 2; //input number {i+1}\n"
    stimulus += f"\n        // Finish simulation\n"
    stimulus += f"        #100 $finish;\n"
    stimulus += f"    end\n\n"

    tb_footer = f"endmodule // {module_name}_TB\n"

    return tb_header + parameters  + signals + dut_instantiation + clock_gen + stimulus + tb_footer




#############################################################################
################################### Main ####################################
#############################################################################


moduleName = valid_module_name().capitalize()
numofinputs = only_integer("Please enter the number of inputs: ")
numofoutputs = only_integer("Please enter the number of outputs: ")

used_names = set()  # To track already used variable names
used_names.add("clk")
used_names.add("reset")
listofinputs = []
listofoutputs = []


print("\n*************Please enter the names of inputs:**************\n")
for i in range(numofinputs):
    inp_signal_name, inp_signal_width = valid_unique_variable_name(moduleName, used_names)
    listofinputs.append((inp_signal_name.capitalize(),inp_signal_width))

print("\n*************Please enter the names of outputs:**************\n")
for i in range(numofoutputs):
    outp_signal_name, outp_signal_width = valid_unique_variable_name(moduleName, used_names)
    listofoutputs.append((outp_signal_name.capitalize(),outp_signal_width))

################################### Generate module and testbench#####################
design_type = valid_design_type()
verilog_module = generate_verilog_template(moduleName, listofinputs, listofoutputs, design_type)
clk_period = only_integer("Enter the clock period in nanosecond: ")
verilog_testbench = generate_testbench_template(moduleName, listofinputs, listofoutputs, clk_period)

################################### Save to files ####################################
with open(f"{moduleName}.v", "w") as module_file:
    module_file.write(verilog_module)

with open(f"{moduleName}_tb.v", "w") as tb_file:
    tb_file.write(verilog_testbench)

print(f"\nVerilog module and testbench for '{moduleName}' have been generated!")
print("***********************************************************************")
print(f"Thank you for using this script, BYE BYE!")


