import os
import sys
import tkinter
import tkinter.messagebox

class Load(object):

    @classmethod
    def config(self):

        def set_command():
            user_name = e_name.get()
            user_email = e_email.get()
            
            # config setting.
            os.system('git config --global --replace-all user.name "{name}"'.format(name = user_name))
            os.system('git config --global --replace-all user.email "{email}"'.format(email = user_email))
            
            tkinter.messagebox.showinfo('提示','设置成功！')
            sys.exit(0)
            
        def cancel_command():
            sys.exit(0)

        user_name = "fengtk"
        user_email = "fengtk@shanghaitech.edu.cn"

        root = tkinter.Tk()
        root.title('初始设置') 
        sw = root.winfo_screenwidth()
        #得到屏幕宽度
        sh = root.winfo_screenheight()
        #得到屏幕高度
        ww = 330
        wh = 130
        x = (sw-ww) / 2
        y = (sh-wh) / 2
        root.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
        #输入框宽度
        width_setting = 35
        
        tk_name = tkinter.StringVar()
        tk_name.set(user_name)
        # 第一行，用户名标签及输入框
        l_name =tkinter.Label(root,text='用户名：')
        l_name.grid(row=0,column=0,sticky=tkinter.W)
        p_name =tkinter.Label(root,text='样例：fengtk')
        p_name.grid(row=1,column=1,sticky=tkinter.W)
        e_name =tkinter.Entry(root, textvariable=tk_name, width = width_setting)
        e_name.grid(row=0,column=1,columnspan=2,sticky=tkinter.W)

        tk_email = tkinter.StringVar()
        tk_email.set(user_email)
        #第二行，邮箱标签及输入框
        l_email = tkinter.Label(root,text='邮箱：')
        l_email.grid(row=2,column=0,sticky=tkinter.W)
        p_email =tkinter.Label(root,text='样例：fengtk@shanghaitech.edu.cn')
        p_email.grid(row=3,column=1,sticky=tkinter.W)
        e_email = tkinter.Entry(root, textvariable=tk_email, width = width_setting)
        e_email.grid(row=2,column=1,columnspan=2,sticky=tkinter.W)

        #第三行设置按扭，command绑定事件
        b_download = tkinter.Button(root,text='   确定   ',command=set_command)
        b_download.grid(row=4,column=1,sticky=tkinter.E)

        b_cancel = tkinter.Button(root,text='   取消   ',command=cancel_command)
        b_cancel.grid(row=4,column=2,sticky=tkinter.E)

        root.mainloop()

    @classmethod
    def download(self):

        def download_command():
            homework_name = e_homework.get()
            name = e_name.get()
            with open("log.txt","w",encoding="utf-8") as f_w:
                f_w.write(homework_name)
                f_w.write("\n")
                f_w.write(name)
                f_w.write("\n")
                f_w.write("1")
            
            # download the homework.
            os.system('git clone http://gitlab.q71998.cn/'+name+'/'+homework_name+'.git')
            
            tkinter.messagebox.showinfo('提示','下载结束！请检查是否下载成功。')
            sys.exit(0)
            
        def cancel_command():
            homework_name = e_homework.get()
            name = e_name.get()
            with open("log.txt","w",encoding="utf-8") as f_w:
                f_w.write(homework_name)
                f_w.write("\n")
                f_w.write(name)
                f_w.write("\n")
                f_w.write("1")
            sys.exit(0)

        homework_name = "homework-2"
        name = "fengtk"

        root = tkinter.Tk()
        root.title('下载作业') 
        sw = root.winfo_screenwidth()
        #得到屏幕宽度
        sh = root.winfo_screenheight()
        #得到屏幕高度
        ww = 250
        wh = 130
        x = (sw-ww) / 2
        y = (sh-wh) / 2
        root.geometry("%dx%d+%d+%d" %(ww,wh,x,y))

        # 检查是否有log文件
        if os.path.exists("log.txt"):
            with open("log.txt","r",encoding="utf-8") as f:
                lines = f.readlines()
            if len(lines) >= 1:
                homework_name = lines[0].strip('\n')
            if len(lines) >= 2:
                name = lines[1].strip('\n')
        
        tk_homework = tkinter.StringVar()
        tk_homework.set(homework_name)
        # 第一行，作业名标签及输入框
        l_homework =tkinter.Label(root,text='作业名：')
        l_homework.grid(row=0,column=0,sticky=tkinter.W)
        p_homework =tkinter.Label(root,text='样例：homework-1')
        p_homework.grid(row=1,column=1,sticky=tkinter.W)
        e_homework =tkinter.Entry(root, textvariable=tk_homework)
        e_homework.grid(row=0,column=1,columnspan=2,sticky=tkinter.W)

        tk_name = tkinter.StringVar()
        tk_name.set(name)
        #第二行，姓名标签及输入框
        l_name = tkinter.Label(root,text='姓名：')
        l_name.grid(row=2,column=0,sticky=tkinter.W)
        p_name =tkinter.Label(root,text='样例：fengtk')
        p_name.grid(row=3,column=1,sticky=tkinter.W)
        e_name = tkinter.Entry(root, textvariable=tk_name)
        e_name.grid(row=2,column=1,columnspan=2,sticky=tkinter.W)

        #第三行下载按扭，command绑定事件
        b_download = tkinter.Button(root,text='   下载   ',command=download_command)
        b_download.grid(row=4,column=1,sticky=tkinter.E)

        b_cancel = tkinter.Button(root,text='   取消   ',command=cancel_command)
        b_cancel.grid(row=4,column=2,sticky=tkinter.E)

        root.mainloop()
    
    @classmethod
    def handin(self):
        
        def handin_command():
            homework_name = e_homework.get()
            name = e_name.get()
            trial_time = int(e_trial.get())

            # 检查
            if trial_time > 30:
                if tkinter.messagebox.askokcancel("警告","尝试次数超过30！您要继续吗？"):
                    pass
                else:
                    return
            
            tag_name = "trial_" + str(trial_time)
            if not(os.path.exists(homework_name)):
                tkinter.messagebox.showwarning('警告','作业文件夹不存在！请重试。')
                return
            
            cur_path = os.getcwd()
            os.chdir("{homework}".format(homework = homework_name))
            os.system("git add .")
            os.system("git commit -m homework_hand_in")
            os.system("git push origin master")
            if not(tkinter.messagebox.askokcancel("警告","已完成上传作业操作。请检查是否成功后继续。\n注意：如果未上传成功并继续仍将消耗可用作业提交次数！")):
                os.chdir(cur_path)
                return
            
            print("\nPlease wait and do not click any buttons!")
            os.system("git tag {tagname} && git push origin {tagname}".format(tagname = tag_name))

            os.chdir(cur_path)
            with open("log.txt","w",encoding="utf-8") as f_w:
                f_w.write(homework_name)
                f_w.write("\n")
                f_w.write(name)
                f_w.write("\n")
                f_w.write(str(trial_time + 1))
             
            tkinter.messagebox.showinfo('提示','提交结束！请检查是否提交成功。')
            sys.exit(0)
            
        def cancel_command():
            homework_name = e_homework.get()
            name = e_name.get()
            trial_time = int(e_trial.get())
            with open("log.txt","w",encoding="utf-8") as f_w:
                f_w.write(homework_name)
                f_w.write("\n")
                f_w.write(name)
                f_w.write("\n")
                f_w.write(str(trial_time))
            sys.exit(0)

        homework_name = "homework-2"
        name = "fengtk"
        trial_time = 1
        
        root = tkinter.Tk()
        root.title('作业提交') 
        sw = root.winfo_screenwidth()
        #得到屏幕宽度
        sh = root.winfo_screenheight()
        #得到屏幕高度
        ww = 270
        wh = 180
        x = (sw-ww) / 2
        y = (sh-wh) / 2
        root.geometry("%dx%d+%d+%d" %(ww,wh,x,y))

        # 检查是否有log文件
        if os.path.exists("log.txt"):
            with open("log.txt","r",encoding="utf-8") as f:
                lines = f.readlines()
            if len(lines) >= 1:
                homework_name = lines[0].strip('\n')
            if len(lines) >= 2:
                name = lines[1].strip('\n')
            if len(lines) >= 3 and lines[2].strip('\n').isdigit():
                trial_time = int(lines[2].strip('\n'))
        
        tk_homework = tkinter.StringVar()
        tk_homework.set(homework_name)
        # 第一行，作业名标签及输入框
        l_homework =tkinter.Label(root,text='作业名：')
        l_homework.grid(row=0,column=0,sticky=tkinter.W)
        p_homework =tkinter.Label(root,text='样例：homework-1')
        p_homework.grid(row=1,column=1,sticky=tkinter.W)
        e_homework =tkinter.Entry(root, textvariable=tk_homework)
        e_homework.grid(row=0,column=1,columnspan=2,sticky=tkinter.W)
        
        tk_name = tkinter.StringVar()
        tk_name.set(name)
        #第二行，姓名标签及输入框
        l_name = tkinter.Label(root,text='姓名：')
        l_name.grid(row=2,column=0,sticky=tkinter.W)
        p_name =tkinter.Label(root,text='样例：fengtk')
        p_name.grid(row=3,column=1,sticky=tkinter.W)
        e_name = tkinter.Entry(root, textvariable=tk_name)
        e_name.grid(row=2,column=1,columnspan=2,sticky=tkinter.W)

        tk_trial = tkinter.StringVar()
        tk_trial.set(str(trial_time))
        #第三行，尝试次数标签及输入框
        l_trial = tkinter.Label(root,text='当前尝试次数：')
        l_trial.grid(row=4,column=0,sticky=tkinter.W)
        p_trial =tkinter.Label(root,text='样例：5')
        p_trial.grid(row=5,column=1,sticky=tkinter.W)
        e_trial = tkinter.Entry(root, textvariable=tk_trial)
        e_trial.grid(row=4,column=1,columnspan=2,sticky=tkinter.W)

        #第三行下载按扭，command绑定事件
        b_download = tkinter.Button(root,text='   提交   ',command=handin_command)
        b_download.grid(row=6,column=1,sticky=tkinter.E)

        b_cancel = tkinter.Button(root,text='   取消   ',command=cancel_command)
        b_cancel.grid(row=6,column=2,sticky=tkinter.E)

        root.mainloop()

if __name__ == "__main__":
    if sys.argv[0] == 'Support.py':
        if sys.argv[1] == '--download':
            Load.download()
        elif sys.argv[1] == '--handin':
            Load.handin()
        elif sys.argv[1] == '--config':
            Load.config()
    else:
        print("Wrong file name! Please get it updated.")