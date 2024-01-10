import tkinter as tk

def calcular(): 
#DESAFIO:
#lógica da calculadora 4 operações básicas 
 pass

root =  tk.Tk()
root.title('JANELA')


text_label =  tk.Label(root, text= 'Calculadora')

text_label1 =  tk.Label(root, text= 'numero 1')
dado_entry = tk.Entry(root, )



text_label2 =  tk.Label(root, text= 'numero 2')
dado_entry2 = tk.Entry(root)


btn  =  tk.Button(root, text='calcular')
mostrar_label = tk.Label(root, text ='')

text_label.pack()
text_label1.pack()
dado_entry.pack()
text_label2.pack()
dado_entry2.pack()
btn.pack()
mostrar_label.pack()
root.mainloop()

