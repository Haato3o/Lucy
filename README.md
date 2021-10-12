# Lucy

Lucy is a programming language based on x64_86 assembly

## Instructions

```x86asm
; Instructions
mov         addr, val
push        val
pop         addr
add         val, val
sub         val, val
mul         val, val
div         val, val
mod         val, val
jne         addr
jmp         addr
je          addr
inc         val
or          val, val
and         val, val
xor         val, val
call        func
ret     

; Built-ins
stdout      val
stdin       val
dmp         val
malloc      reg
free        ptr

; Registers
rax
rbx
rcx
rdx
rsi
rdi
rsp
rbp
```