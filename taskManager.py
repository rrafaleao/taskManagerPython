from tkinter import *

class Task:
    def __init__(self, id, titulo, desc, status):
        self.id = id
        self.titulo = titulo
        self.desc = desc
        self.status = status

class Task_manager:
    def __init__(self):
        self.task = []

    def add_task(self, task):
        self.task.append(task)

    def remove_task(self, id):
        for task in self.task:
            if task.id == id:
                self.task.remove(task)
                return True
        return False

class Interface:
    def __init__(self, janela):
        self.janela = janela
        self.task = Task_manager()
        self.janela_principal = Frame(janela)
        self.janela_principal.pack()

        Add_task = Button(self.janela_principal, text=("Adicionar nova tarefa"), font=("Gulim",15), width=20,height=3, command=self.Add_task)
        Add_task.pack()
        Show_task = Button(self.janela_principal, text=("Visualizar tarefas"), font=("Gulim",15), width=20,height=3, command=self.View_task)
        Show_task.pack()
        Edit_task = Button(self.janela_principal, text=("Editar tarefas"), font=("Gulim",15), width=20,height=3, command=self.edit_task)
        Edit_task.pack()
        Remove_task = Button(self.janela_principal, text=("Remover tarefas"), font=("Gulim",15), width=20,height=3, command=self.remove_task)
        Remove_task.pack()

    def Add_task(self):
        self.janela_principal.pack_forget()
        Add_task_frame = Frame(self.janela)
        Add_task_frame.pack()

        id_label = Label(Add_task_frame, text="Id:", font=("Gulim",11), width=6,height=2)
        id_label.pack()
        id_entry = Entry(Add_task_frame)
        id_entry.pack()

        titulo_label = Label(Add_task_frame, text="Título:", font=("Gulim",11), width=6,height=2)
        titulo_label.pack()
        titulo_entry = Entry(Add_task_frame)
        titulo_entry.pack()

        desc_label = Label(Add_task_frame, text="Descrição:", font=("Gulim",11), width=7,height=2)
        desc_label.pack()
        desc_entry = Entry(Add_task_frame)
        desc_entry.pack()

        status_label = Label(Add_task_frame, text="Status:", font=("Gulim",11), width=6,height=2)
        status_label.pack()
        status_entry = Entry(Add_task_frame)
        status_entry.pack()

        def salvar_task():
            id = id_entry.get()
            titulo = titulo_entry.get()
            desc = desc_entry.get()
            status = status_entry.get()
            new_task = Task(id, titulo, desc, status)
            self.task.add_task(new_task)
            Add_task_frame.pack_forget()
            self.janela_principal.pack()

        salvar = Button(Add_task_frame, text=("Salvar"),font=("Gulim",11), width=6,height=2,command= salvar_task)
        salvar.pack()

        voltar = Button(Add_task_frame, text=("Voltar"), font=("Gulim",11), width=6,height=2,command=lambda: self.voltar(Add_task_frame))
        voltar.pack()

    def View_task(self):
        self.janela_principal.pack_forget()
        View_task_frame = Frame(self.janela)
        View_task_frame.pack()
        
        for task in self.task.task:
            task_label = Label(View_task_frame, text=f"Id: {task.id}, Titulo: {task.titulo}, Descrição: {task.desc}, Status: {task.status}", font=("Gulim",11))
            task_label.pack()

        voltar = Button(View_task_frame, text=("Voltar"), font=("Gulim",11), width=6,height=2,command=lambda: self.voltar(View_task_frame))
        voltar.pack()

    def edit_task(self):
        self.janela_principal.pack_forget()
        edit_task_frame = Frame(self.janela)
        edit_task_frame.pack()

        id_busca_label = Label(edit_task_frame, text="ID da tarefa a ser editada:", font=("Gulim",11), width=20, height=2)
        id_busca_label.pack()
        id_busca_entry = Entry(edit_task_frame)
        id_busca_entry.pack()

        def buscar_tarefa():
            id_busca = id_busca_entry.get()
            tarefa_encontrada = None

            for task in self.task.task:
                if task.id == id_busca:
                    tarefa_encontrada = task
                    break

            if tarefa_encontrada:
                id_label = Label(edit_task_frame, text="Novo Id:", font=("Gulim",11), width=15, height=2)
                id_label.pack()
                id_entry = Entry(edit_task_frame)
                id_entry.insert(0, tarefa_encontrada.id)
                id_entry.pack()

                titulo_label = Label(edit_task_frame, text="Novo Título:", font=("Gulim",11), width=15, height=2)
                titulo_label.pack()
                titulo_entry = Entry(edit_task_frame)
                titulo_entry.insert(0, tarefa_encontrada.titulo)
                titulo_entry.pack()

                desc_label = Label(edit_task_frame, text="Nova Descrição:", font=("Gulim",11), width=15, height=2)
                desc_label.pack()
                desc_entry = Entry(edit_task_frame)
                desc_entry.insert(0, tarefa_encontrada.desc)
                desc_entry.pack()

                status_label = Label(edit_task_frame, text="Novo Status:", font=("Gulim",11), width=15, height=2)
                status_label.pack()
                status_entry = Entry(edit_task_frame)
                status_entry.insert(0, tarefa_encontrada.status)
                status_entry.pack()

                def salvar_task_editada():
                    tarefa_encontrada.id = id_entry.get()
                    tarefa_encontrada.titulo = titulo_entry.get()
                    tarefa_encontrada.desc = desc_entry.get()
                    tarefa_encontrada.status = status_entry.get()

                    edit_task_frame.pack_forget()
                    self.janela_principal.pack()

                salvar = Button(edit_task_frame, text=("Salvar Alterações"), font=("Gulim",11), width=15, height=2, command=salvar_task_editada)
                salvar.pack()
            else:
                erro = Label(edit_task_frame, text="Tarefa não encontrada", font=("Gulim",11))
                erro.pack()

        buscar = Button(edit_task_frame, text=("Buscar Tarefa"), font=("Gulim",11), width=12, height=2, command=buscar_tarefa)
        buscar.pack()

        voltar = Button(edit_task_frame, text=("Voltar"), font=("Gulim",11), width=6, height=2, command=lambda: self.voltar(edit_task_frame))
        voltar.pack()

    def remove_task(self):
        self.janela_principal.pack_forget()
        remove_task_frame = Frame(self.janela)
        remove_task_frame.pack()

        id_busca_label = Label(remove_task_frame, text="ID da tarefa que quer remover:", font=("Gulim",11), width=27, height=2)
        id_busca_label.pack()
        id_busca_entry = Entry(remove_task_frame)
        id_busca_entry.pack()

        def remover_task():
            id = id_busca_entry.get()
            sucesso = self.task.remove_task(id)
            
            if sucesso:
                msg = Label(remove_task_frame, text="Tarefa removida com sucesso!", font=("Gulim",11), fg="green")
            else:
                msg = Label(remove_task_frame, text="Tarefa não encontrada!", font=("Gulim",11), fg="red")
            msg.pack()

            remove_task_frame.pack_forget()
            self.janela_principal.pack()

        buscar = Button(remove_task_frame, text=("Apagar Tarefa"), font=("Gulim",11), width=12, height=2, command=remover_task)
        buscar.pack()

        voltar = Button(remove_task_frame, text=("Voltar"), font=("Gulim",11), width=6, height=2, command=lambda: self.voltar(remove_task_frame))
        voltar.pack()

    def voltar(self, frame):
        frame.pack_forget()
        self.janela_principal.pack()

janela = Tk()
App = Interface(janela)
janela.geometry("800x600")
janela.title("Task Manager")
janela.mainloop()