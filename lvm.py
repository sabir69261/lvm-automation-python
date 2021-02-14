import os

print("\t\t\tWelcome to menu driven program........")
while True:
 
    choice =input("Enter your choice:  ")
    
    if (("show" in choice) and ((("physical" in choice) and ("volume" in choice)) or ("pv" in choice))):
        os.system("pvdisplay")     
    elif (("create" in choice) and ((("physical" in choice) and ("volume" in choice)) or ("pv" in choice))):
        hddname = input("Enter hdd name : ")
        os.system("pvcreate {} " .format(hddname))
    elif (("show" in choice) and ((("volume" in choice) and ("group" in choice)) or ("vg" in choice))):
        os.system("vgdisplay")
    elif (("create" in choice) and ((("volume" in choice) and ("group" in choice)) or ("vg" in choice))):
        vgname = input("Enter VG name : ")
        pvname = input("Enter PV name : ")
        os.system("vgcreate {} {} " .format(vgname, pvname))
    elif (("show" in choice) and ((("logical" in choice) and ("volume" in choice)) or ("lv" in choice))):
        os.system("lvdisplay")
    elif ("show" in choice) and ("hdd" in choice):
        os.system("fdisk -l")
    elif (("create" in choice) and ((("logical" in choice) and ("volume" in choice)) or ("lv" in choice))):
        size = input("Partion size :  ")
        name = input("Partion name :  ")
        vgname = input("VG name:  ")
        os.system("lvcreate --size {}  --name {}  {}" .format(size,name,vgname))
        os.system("mkfs.ext4 /dev/{}/{}" .format(vgname,name))
        os.system("udevadm settle")  
        print("logical partiton created\nif you want to mount this partition you can give input : mount logical volume")
    elif (("mount" in choice) and ((("logical" in choice) and ("volume" in choice)) or  ("lv" in choice))):
        partition_name = input("ENter your partion name : ")
        mount_point = input("Enter mount point : ")
        os.system("mount {} {} " .format(partition_name , mount_point))

    elif (("extend" in choice) or ("increase" in choice)) and ("partition" in choice) and ("size" in choice):
        size = input("Extend Size : ")
        partition = input("Enter Partition Name: ")
        #vgname = input("Enter VG Name : ")
        os.system("lvextend --size +{}G {} " .format(size, partition)) 
        os.system("resize2fs {}" .format(partition))
        print("Partition size extend successfully")
    elif (("reduce" in choice) or ("decrease" in choice))  and ("partition" in choice) and ("size"):
        mount_point = input("Enter partition mount point : ")
        partition_name = input("Enter partition name : ")
        size = input("Enter the size to scan : ")
        reduce_size = input("Enter the size for reduce : ")
        os.system("umount {} " .format(mount_point))
        os.system("e2fsck -f {}" .format(partition_name))
        os.system("resize2fs {} {}" .format(partition_name, size)) 
        os.system("lvreduce --size -{} {}" .format(reduce_size, partition_name))
       # os.system("e2fsck -f {}" .format(partition_name))
        os.system("mount {} {} " .format(partition_name, mount_point))
    elif ("show" in choice) and ("partition" in choice) and ("mount" in  choice):
        os.system("df -hT")
    elif ("show" in choice) and ("created" in choice) and ("partition" in choice):
        os.system("lsblk")
    elif ("stop" in choice) or ("exit" in choice):
        break
    
    else:
        print("not support pls try again")

