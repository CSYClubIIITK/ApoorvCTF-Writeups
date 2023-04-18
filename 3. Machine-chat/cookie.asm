bits 16

mov ah, 1
mov al, 0
mov ax, 0

pop ax
call print_rax
call print_info

mov bh, 0
mov bl, 0
mov bx, 0 

mov ch, 1
mov cl, 1
mov cx, 0x5E2


xor dh, dh  
and dl, 0
mov dx, 0x277E
not dx



mov ds, ax 
mov es, bx
mov fs, cx 
mov gs, dx 
mov ss, ax



mov sp, cx 
mov bp, dx 
mov si, sp 
mov di, bp

print_string:
  .init:
    mov si, ax

  


mov bp, 
mov dh, 3   
mov dl, 15  
mov cx, 0x0007   
mov bx, 0000000000001111b  



mov al, 0X4C9
mov ah, 0X4D5 

 push cx
        push dx
          push ax
            xor cx, cx
            mov dx, 0xffff
            mov ah, 0x86
            int 0x15
          pop ax
        pop dx
      pop cx





  mov ax, 2
      push ax
        call print_rax
        call print_info  

        mov ax, 3
        push ax
          call print_rax 
          call print_info  

          mov ax, 4
          push ax
            call print_rax
            call print_info

            mov ax, 5
            push ax
              call print_rax
              call print_info

          pop ax  
          call print_rax
          call print_info  

        pop ax
        call print_rax



daps:
  .size:             db 0x10
  db 0 ; always 0
  .num_sectors:      dw NUM_SECTORS 
   from the environment, see the makefile
  .transfer_buffer:  dd LOAD_ADDR
  .lba_lower:        dd 0x1
  .lba_upper:        dd 0x0

times 0200h - 2 - ($ - $$)  db 0    510 bytes
dw 0AA55h              