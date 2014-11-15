import sys
# simulate the cells with a list
tape = [0]*(3*10**4)
# the data pointer
ptr = 0

def lt():
    """ performs a < """
    global ptr
    if ptr <= 0:
        raise ValueError, "Segmentation fault!"
    ptr -= 1
 
def gt():
    """" performs a > """
    global ptr
    if ptr >= 3*10**4 - 1:
        raise ValueError, "Segmentation fault!"
    ptr += 1

def plus():
    """ performs a + """
    global ptr
    tape[ptr] = (tape[ptr] + 1) % 256
 
def minus():
    """ perfoms a - """
    global ptr
    tape[ptr] = (tape[ptr] - 1) % 256

def dot():
    """ performs a . """
    global ptr
    sys.stdout.write(chr(tape[ptr]))
 
def comma():
    """ performs a , """
    global ptr
    c = ord(sys.stdin.read(1))
    if c != 26:
        tape[ptr] = c

def parse(code):
    """ maps the "["s to the corresponding "]"s """
    # stack to contain the indices of the opening brackets
    opening = []
    # dict which maps the indices of the opening brackets
    # to the closing brackets
    loop = {}
    for i,c in enumerate(code):
        if c == "[":
            opening.append(i)
        elif c == "]":
            try:
                begin = opening.pop()
                loop[begin] = i
            except IndexError:
                raise ValueError, "Supplied string isn't balanced, too many ]s!"
    # if the stack isn't empty, the string cannot be balanced
    if opening != []:
        raise ValueError, "Supplied string isn't balanced, too many [s"
    else:
        return loop

# primitives which can directly be handled
handle_directly = { "okay" : dot, "okaay" : comma, "okaaay" : lt, "okaaaay" : gt, "okaaaaay" : plus, "okaaaaaay" : minus}
 
 
def eval_bf(code):
    """ evaluates brainfuck code """
    global ptr
    # get the scopes of the "[", "]"s
    loop = parse(code)
    # initialize the program counter
    pc = 0
    # a stack to store the pc for loops
    stack = []
    while pc < len(code):
        instruction = code[pc] if (code[pc] == ']' or code[pc] == '[') else code[pc:(code[pc::].find("y")+1+pc)]
        inc = 1 if code[pc] == ']' or code[pc] == '[' else len(code[pc:(code[pc::].find("y"))+1+pc])
        # handle the primitives directly
        if instruction in handle_directly.keys():
            apply(handle_directly[instruction])
        elif instruction == "[":
            # if loop condition is fullfiled
            # enter loop block
            if tape[ptr] > 0:
                stack.append(pc)
            else: # else go to the end of the block
                pc = loop[pc]
        elif instruction == "]":
            # jump back where you came from!
            pc = stack.pop() - 1
        pc += inc

if __name__ == '__main__':
    try:
        data = open(sys.argv[1]).read()
        eval_bf(data)
    except IndexError:
        print "Entering REPL mode"
        while True:
            try:
                print "Okay >>",
                eval_bf(raw_input())
                ptr = 0
                tape = [0]*(3*10**4)
            except KeyboardInterrupt:
                print "\nOkay >>",
                eval_bf(raw_input())
                ptr = 0
                tape = [0]*(3*10**4)
