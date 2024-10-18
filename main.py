import printer

p=printer.ThermalPrinter(serialport="/dev/usb/lp0") 
p.print_text("\nHello Geek Gurl Diaries viewers!What happens if we try to print a longer sentence or paragraph? Will it go over multiple lines or will the text just be cut off? It's good to test these things you know!\n") 
p.linefeed() 
p.linefeed()
p.linefeed()
