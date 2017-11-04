import subprocess,os,time

def main():
        val=0
        subprocess.call("top -b -n 1 | sed -n '7,$p' |  awk '{print $1,$2,$4,$9,$12}' | grep '%s\.[[:digit:]]' > top_result.txt" %val,shell=True)
        f_cat=subprocess.Popen("cat top_result.txt",shell=True,stdout=subprocess.PIPE)
        count=subprocess.Popen("wc -l", shell=True,stdin=f_cat.stdout,stdout=subprocess.PIPE)
        print("Number of processes is {0}" .format(count.communicate()[0].decode()))
        f=open('top_result.txt','r')
        for lines in f.readlines():
                j=lines.strip().split(' ')
                print("{0} has CPU usage {1}, nice value {2}, user is {3}" .format(j[4],j[3],j[2],j[1]))
                print("\n")
                a=raw_input("Do you want to change nice value ? [y/n]. Press [q/Q] for exit: ")
                if(a=='n' or a=='N'):
                        pass
                elif(a=='y' or a=='Y'):
                         new_nice=raw_input("Enter new nice value: ")
                         n_nice=subprocess.Popen("renice {0} {1}" .format(new_nice,j[0]),shell=True,stdout=subprocess.PIPE)
                         print("RESULT: {0}" .format(n_nice.communicate()[0].decode()))
                         print("Sucessfully changed!")
                         time.sleep(1)
                elif(a=='q' or a=='Q'):
                        break
                else:
                        os.system("clear")
                        print("Cannot recognise input")
                        time.sleep(2)
                os.system("clear")
        print("Completed")
        f.close()


if __name__=='__main__':
        main()
