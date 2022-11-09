# Classes the we want to represent in database
class Node:
    def __init__(self,type,name,loadsetTypeRef, redundant, platformRef, syncLostBehavior):
        self.type = type
        self.name = name
        self.loadsetTypeRef = loadsetTypeRef
        self.redundant = redundant
        self.platformRef = platformRef
        self.syncLostBehavior =  syncLostBehavior
        self.cpus = []
    def reprJSON(self):
        return {"name":self.name,"load_set_type":self.loadsetTypeRef,"redundant":self.redundant,
                "platform":self.platformRef,"sync_loss":self.syncLostBehavior,"cpu_set":self.cpus}

class Cpu:
    def __init__(self,name,type, unitid, IOPRef, ACCSSyncMaster,domainBorder):
        self.name = name    #node of origin/parent node
        self.type = type    #"APP" or "IOP"
        self.unitid = unitid
        self.IOPRef = IOPRef
        self.ACCSSyncMaster = ACCSSyncMaster
        self.domainBorder = domainBorder
        self.applications = []
        self.partitions = []
    def reprJSON(self):
        return {"name":self.name,"type":self.type,"unit_id":self.unitid,"iop_ref":self.IOPRef,
        "accs_sync_master":self.ACCSSyncMaster,"domain_border":self.domainBorder,"partition_set":self.partitions,"application_set":self.applications}


class Partition_Data_Class:
    def __init__(self,name,ltmbool,id, node,cpu):
        self.name = name
        self.isLTM = ltmbool
        #Denna va med i project 1... lol?
        self.fixedStartNs = None
        self.partiton_id = id
        self.nodename = node
        self.cpuname = cpu
        self.applications = []
    def reprJSON(self):
        return {"name":self.name,"is_ltm":self.isLTM,"partition_id":self.partiton_id,
                "application_set":self.applications,"fixed_start":self.fixedStartNs}

class Application:
    #<DipsApplication name="Port_Gateway_1" rampool="0x10000" instanceOf="port_gateway" affinity="0"/>
    def __init__(self,name, rampool, instanceOf, affinity,node,cpu,partition):
        self.name = name
        self.rampool = rampool
        self.instanceOf = instanceOf
        self.affinity = affinity
        self.nodename = node
        self.cpuname = cpu
        self.partitionname = partition

    def reprJSON(self):
        return {"name":self.name,"cpu":None} #,"rampool":self.rampool,"instanceOf":self.instanceOf,"affinity":self.affinity}

class Application_Instances:
    def __init__(self,name, instanceOf):
        self.name = name
        self.instanceOf = instanceOf
    
    def reprJSON(self):
        return {"name":self.name}
    
class ApplicationContainer:
    def __init__(self,name):
        self.name = name
        self.applicationlist = []
    
    def reprJSON(self):
        return {"name":self.name,"applicaitonlist":self.applicationlist}
class Connection:
    
    def __init__(self, Provider_name, Provider_Application, Requirer_name, Requirer_Application):
        self.Provider_name = Provider_name
        self.Requirer_name = Requirer_name
        self.Provider_Application = Provider_Application
        self.Requirer_Application = Requirer_Application
        
    def reprJSON(self):
        return {"Provider_name":self.Provider_name,"Provider_Application":self.Provider_Application,
        "Requirer_name":self.Requirer_name, "Requirer_Application":self.Requirer_Application} 

class ConnectionContainer:
    def __init__(self,projectname):
        self.project_name = projectname
        self.connectionlist = []
    
    def reprJSON(self):
        return {"project_name":self.project_name,"connectionlist":self.connectionlist}

#The lists should contain Objects of the Objects

class Project_Data_Class:
    def __init__(self,name):
        self.name = name
        self.node_set = []
    def reprJSON(self):
        return {"name":self.name,"node_set":self.node_set}
         
    def insert_partitions(self,partitionlist):
        for partition in partitionlist:
            for node in self.node_set:
                if partition.nodename == node.name:
                    for cpu in node.cpus:
                        if partition.cpuname == cpu.name:
                            cpu.partitions.append(partition)   
    
    def insert_applications(self,applicationlist):
        
        for application in applicationlist:
            for node in self.node_set:
                if application.nodename == node.name:
                    for cpu in node.cpus:
                        if application.cpuname == cpu.name:
                            if(application.partitionname == None):
                                cpu.applications.append(application)
                            #cpu.partitions.append(partition)  
    
    def filter(self,objectlist):
        
        for objecttype in objectlist:
            #if isinstance(object,Cpu):
            #    self.Cpu.append(object)
            if isinstance(objecttype, Node):
                self.node_set.append(objecttype)
            #elif isinstance(object, Partitions):
            #    self.Partitions.append(object)