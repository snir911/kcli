# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kcli.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nkcli.proto\"\x07\n\x05\x65mpty\"/\n\x07version\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x13\n\x0bgit_version\x18\x02 \x01(\t\"\xd7\x03\n\x06\x63lient\x12\x0e\n\x06\x63lient\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0f\n\x07\x63urrent\x18\x03 \x01(\x08\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x15\n\raccess_key_id\x18\x05 \x01(\t\x12\x19\n\x11\x61\x63\x63\x65ss_key_secret\x18\x06 \x01(\t\x12\x0e\n\x06region\x18\x07 \x01(\t\x12\x0f\n\x07keypair\x18\x08 \x01(\t\x12\x0c\n\x04host\x18\t \x01(\t\x12\x0c\n\x04port\x18\n \x01(\t\x12\x0c\n\x04user\x18\x0b \x01(\t\x12\x10\n\x08protocol\x18\x0c \x01(\t\x12\x0b\n\x03url\x18\r \x01(\t\x12\x0c\n\x04pool\x18\x0e \x01(\t\x12\x12\n\ndatacenter\x18\x0f \x01(\t\x12\x0f\n\x07\x63\x61_file\x18\x10 \x01(\t\x12\x0f\n\x07\x63luster\x18\x11 \x01(\t\x12\x0b\n\x03org\x18\x12 \x01(\t\x12\x10\n\x08password\x18\x13 \x01(\t\x12\x13\n\x0b\x63redentials\x18\x14 \x01(\t\x12\x0f\n\x07project\x18\x15 \x01(\t\x12\x0c\n\x04zone\x18\x16 \x01(\t\x12\x0e\n\x06\x64omain\x18\x17 \x01(\t\x12\x10\n\x08\x61uth_url\x18\x18 \x01(\t\x12\r\n\x05token\x18\x19 \x01(\t\x12\x0e\n\x06multus\x18\x1a \x01(\x08\x12\x0b\n\x03\x63\x64i\x18\x1b \x01(\x08\x12\x0f\n\x07\x65nabled\x18\x1c \x01(\x08\"\'\n\x0b\x63lientslist\x12\x18\n\x07\x63lients\x18\x01 \x03(\x0b\x32\x07.client\"\x86\x01\n\x02vm\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05\x64\x65\x62ug\x18\x02 \x01(\x08\x12\x11\n\tsnapshots\x18\x03 \x01(\x08\x12\x0c\n\x04user\x18\x04 \x01(\t\x12\t\n\x01l\x18\x05 \x01(\t\x12\t\n\x01r\x18\x06 \x01(\t\x12\t\n\x01X\x18\x07 \x01(\x08\x12\t\n\x01Y\x18\x08 \x01(\x08\x12\t\n\x01\x44\x18\t \x01(\t\x12\x0b\n\x03\x63md\x18\n \x01(\t\"-\n\x08snapshot\x12\x10\n\x08snapshot\x18\x01 \x01(\t\x12\x0f\n\x07\x63urrent\x18\x02 \x01(\x08\"A\n\x07netinfo\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\t\x12\x0b\n\x03mac\x18\x02 \x01(\t\x12\x0b\n\x03net\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\"T\n\x08\x64iskinfo\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\t\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\x05\x12\x0c\n\x04type\x18\x05 \x01(\t\"\xcc\x04\n\x06vminfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\t\x12\x0c\n\x04\x63pus\x18\x03 \x01(\x05\x12\x0e\n\x06memory\x18\x04 \x01(\x05\x12\x0c\n\x04plan\x18\x05 \x01(\t\x12\x0f\n\x07profile\x18\x06 \x01(\t\x12\x0e\n\x06status\x18\x07 \x01(\t\x12\n\n\x02ip\x18\x08 \x01(\t\x12\x16\n\x04nets\x18\t \x03(\x0b\x32\x08.netinfo\x12\x18\n\x05\x64isks\x18\n \x03(\x0b\x32\t.diskinfo\x12\x14\n\x0c\x63reationdate\x18\x0b \x01(\t\x12\x0c\n\x04user\x18\x0c \x01(\t\x12\x11\n\tautostart\x18\r \x01(\x08\x12\r\n\x05\x64\x65\x62ug\x18\x0e \x01(\t\x12\x1c\n\tsnapshots\x18\x0f \x03(\x0b\x32\t.snapshot\x12\x0c\n\x04kube\x18\x10 \x01(\t\x12\x10\n\x08kubetype\x18\x11 \x01(\t\x12\x12\n\ninstanceid\x18\x12 \x01(\t\x12\x0c\n\x04host\x18\x13 \x01(\t\x12\x12\n\nprivate_ip\x18\x14 \x01(\t\x12\n\n\x02\x61z\x18\x15 \x01(\t\x12\x0e\n\x06\x66lavor\x18\x16 \x01(\t\x12\x0c\n\x04tags\x18\x17 \x01(\t\x12\x10\n\x08nodeport\x18\x18 \x01(\t\x12\x11\n\tnamespace\x18\x19 \x01(\t\x12\x14\n\x0cloadbalancer\x18\x1a \x01(\t\x12\r\n\x05\x65rror\x18\x1b \x01(\t\x12\r\n\x05owner\x18\x1c \x01(\t\x12\n\n\x02id\x18\x1d \x01(\t\x12\x0f\n\x07project\x18\x1e \x01(\t\x12\x0e\n\x06\x64omain\x18\x1f \x01(\t\x12\x0b\n\x03iso\x18  \x01(\t\x12\x16\n\x0eloadbalancerip\x18! \x01(\t\x12\x0b\n\x03ips\x18\" \x03(\t\"\x1e\n\x06vmlist\x12\x14\n\x03vms\x18\x01 \x03(\x0b\x32\x07.vminfo\"G\n\x06result\x12\x0e\n\x06result\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\x11\n\tdeletedvm\x18\x03 \x03(\t\x12\n\n\x02vm\x18\x04 \x01(\t\"\xad\x01\n\x07profile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x66lavor\x18\x02 \x01(\t\x12\x0c\n\x04pool\x18\x03 \x01(\t\x12\r\n\x05\x64isks\x18\x04 \x01(\t\x12\r\n\x05image\x18\x05 \x01(\t\x12\x0c\n\x04nets\x18\x06 \x01(\t\x12\x11\n\tcloudinit\x18\x07 \x01(\x08\x12\x0e\n\x06nested\x18\x08 \x01(\x08\x12\x12\n\nreservedns\x18\t \x01(\x08\x12\x13\n\x0breservehost\x18\n \x01(\x08\"*\n\x0cprofileslist\x12\x1a\n\x08profiles\x18\x01 \x03(\x0b\x32\x08.profile\"\x18\n\x08isoslist\x12\x0c\n\x04isos\x18\x01 \x03(\t\"\x16\n\x05image\x12\r\n\x05image\x18\x01 \x01(\t\"\x1c\n\nimageslist\x12\x0e\n\x06images\x18\x01 \x03(\t\"0\n\x04\x64isk\x12\x0c\n\x04\x64isk\x18\x01 \x01(\t\x12\x0c\n\x04pool\x18\x02 \x01(\t\x12\x0c\n\x04path\x18\x03 \x01(\t\"!\n\tdiskslist\x12\x14\n\x05\x64isks\x18\x01 \x03(\x0b\x32\x05.disk\"!\n\x04plan\x12\x0c\n\x04plan\x18\x01 \x01(\t\x12\x0b\n\x03vms\x18\x02 \x01(\t\"!\n\tplanslist\x12\x14\n\x05plans\x18\x01 \x03(\x0b\x32\x05.plan\")\n\x07keyword\x12\x0f\n\x07keyword\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"*\n\x0ckeywordslist\x12\x1a\n\x08keywords\x18\x01 \x03(\x0b\x32\x08.keyword\"P\n\x04pool\x12\x0c\n\x04pool\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0c\n\x04\x66ull\x18\x03 \x01(\x08\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x10\n\x08thinpool\x18\x05 \x01(\x08\"!\n\tpoolslist\x12\x14\n\x05pools\x18\x01 \x03(\x0b\x32\x05.pool\"\x9c\x01\n\x07network\x12\x0f\n\x07network\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04\x63idr\x18\x03 \x01(\t\x12\x0c\n\x04\x64hcp\x18\x04 \x01(\t\x12\x0e\n\x06\x64omain\x18\x05 \x01(\t\x12\x0c\n\x04mode\x18\x06 \x01(\t\x12\x0c\n\x04plan\x18\x07 \x01(\t\x12\n\n\x02ip\x18\x08 \x01(\t\x12\x0b\n\x03nat\x18\t \x01(\x08\x12\x11\n\toverrides\x18\n \x01(\t\"*\n\x0cnetworkslist\x12\x1a\n\x08networks\x18\x01 \x03(\x0b\x32\x08.network\"C\n\x06subnet\x12\x0e\n\x06subnet\x18\x01 \x01(\t\x12\n\n\x02\x61z\x18\x02 \x01(\t\x12\x0c\n\x04\x63idr\x18\x03 \x01(\t\x12\x0f\n\x07network\x18\x04 \x01(\t\"\'\n\x0bsubnetslist\x12\x18\n\x07subnets\x18\x01 \x03(\x0b\x32\x07.subnet\"/\n\x04kube\x12\x0c\n\x04kube\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0b\n\x03vms\x18\x03 \x01(\t\"!\n\tkubeslist\x12\x14\n\x05kubes\x18\x01 \x03(\x0b\x32\x05.kube\"M\n\x02lb\x12\n\n\x02lb\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x10\n\x08protocol\x18\x03 \x01(\t\x12\r\n\x05ports\x18\x04 \x01(\t\x12\x0e\n\x06target\x18\x05 \x01(\t\"\x1b\n\x07lbslist\x12\x10\n\x03lbs\x18\x01 \x03(\x0b\x32\x03.lb\"9\n\x06\x66lavor\x12\x0e\n\x06\x66lavor\x18\x01 \x01(\t\x12\x0f\n\x07numcpus\x18\x02 \x01(\x05\x12\x0e\n\x06memory\x18\x03 \x01(\x05\"\'\n\x0b\x66lavorslist\x12\x18\n\x07\x66lavors\x18\x01 \x03(\x0b\x32\x07.flavor\"!\n\x04repo\x12\x0c\n\x04repo\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\"!\n\treposlist\x12\x14\n\x05repos\x18\x01 \x03(\x0b\x32\x05.repo\"l\n\x07product\x12\x0f\n\x07product\x18\x01 \x01(\t\x12\x0c\n\x04repo\x18\x02 \x01(\t\x12\r\n\x05group\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0e\n\x06numvms\x18\x05 \x01(\t\x12\x0e\n\x06memory\x18\x06 \x01(\t\"*\n\x0cproductslist\x12\x1a\n\x08products\x18\x01 \x03(\x0b\x32\x08.product\".\n\x06\x63onfig\x12\x0e\n\x06\x63lient\x18\x01 \x01(\t\x12\x14\n\x0c\x65xtraclients\x18\x02 \x03(\t\"{\n\tcontainer\x12\x11\n\tcontainer\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\x12\r\n\x05image\x18\x03 \x01(\t\x12\x0c\n\x04plan\x18\x04 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x05 \x01(\t\x12\r\n\x05ports\x18\x06 \x01(\t\x12\x0e\n\x06\x64\x65ploy\x18\x07 \x01(\t\"0\n\x0e\x63ontainerslist\x12\x1e\n\ncontainers\x18\x01 \x03(\x0b\x32\n.container\"\x18\n\x06sshcmd\x12\x0e\n\x06sshcmd\x18\x01 \x01(\t\"\x12\n\x03\x63md\x12\x0b\n\x03\x63md\x18\x01 \x01(\t\"r\n\nscpdetails\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x03 \x01(\t\x12\x0c\n\x04user\x18\x04 \x01(\t\x12\x11\n\trecursive\x18\x05 \x01(\x08\x12\x10\n\x08\x64ownload\x18\x06 \x01(\x08\")\n\x06vmfile\x12\x0e\n\x06origin\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\"\xa1\x01\n\tvmprofile\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07profile\x18\x02 \x01(\t\x12\r\n\x05image\x18\x03 \x01(\t\x12\x15\n\rcustomprofile\x18\x04 \x01(\t\x12\x11\n\toverrides\x18\x05 \x01(\t\x12\x0c\n\x04wait\x18\x06 \x01(\x08\x12\x18\n\x07vmfiles\x18\x07 \x03(\x0b\x32\x07.vmfile\x12\x14\n\x0cignitionfile\x18\x08 \x01(\t2\xe8\x05\n\x04Kcli\x12\x16\n\x07\x63onsole\x12\x03.vm\x1a\x04.cmd\"\x00\x12\x16\n\x04info\x12\x03.vm\x1a\x07.vminfo\"\x00\x12\x1a\n\x04list\x12\x07.client\x1a\x07.vmlist\"\x00\x12\"\n\nlist_disks\x12\x06.empty\x1a\n.diskslist\"\x00\x12&\n\x0clist_flavors\x12\x06.empty\x1a\x0c.flavorslist\"\x00\x12$\n\x0blist_images\x12\x06.empty\x1a\x0b.imageslist\"\x00\x12(\n\rlist_networks\x12\x06.empty\x1a\r.networkslist\"\x00\x12 \n\tlist_isos\x12\x06.empty\x1a\t.isoslist\"\x00\x12\"\n\nlist_pools\x12\x06.empty\x1a\n.poolslist\"\x00\x12&\n\x0clist_subnets\x12\x06.empty\x1a\x0c.subnetslist\"\x00\x12\x19\n\x07restart\x12\x03.vm\x1a\x07.result\"\x00\x12\x1d\n\x0eserial_console\x12\x03.vm\x1a\x04.cmd\"\x00\x12\x15\n\x03ssh\x12\x03.vm\x1a\x07.sshcmd\"\x00\x12\x1d\n\x03scp\x12\x0b.scpdetails\x1a\x07.sshcmd\"\x00\x12\x17\n\x05start\x12\x03.vm\x1a\x07.result\"\x00\x12\x16\n\x04stop\x12\x03.vm\x1a\x07.result\"\x00\x12\x18\n\x06\x64\x65lete\x12\x03.vm\x1a\x07.result\"\x00\x12\x1c\n\nget_lastvm\x12\x07.client\x1a\x03.vm\"\x00\x12!\n\x0c\x64\x65lete_image\x12\x06.image\x1a\x07.result\"\x00\x12%\n\x0e\x63reate_network\x12\x08.network\x1a\x07.result\"\x00\x12%\n\x0e\x64\x65lete_network\x12\x08.network\x1a\x07.result\"\x00\x12\x1f\n\x0b\x63reate_pool\x12\x05.pool\x1a\x07.result\"\x00\x12\x1f\n\x0b\x64\x65lete_pool\x12\x05.pool\x1a\x07.result\"\x00\x32\xc4\x08\n\x07Kconfig\x12\"\n\tcreate_vm\x12\n.vmprofile\x1a\x07.result\"\x00\x12\x1f\n\nget_config\x12\x06.empty\x1a\x07.config\"\x00\x12!\n\x0bget_version\x12\x06.empty\x1a\x08.version\"\x00\x12!\n\x0b\x63reate_host\x12\x07.client\x1a\x07.result\"\x00\x12!\n\x0b\x64\x65lete_host\x12\x07.client\x1a\x07.result\"\x00\x12)\n\x10\x64\x65lete_container\x12\n.container\x1a\x07.result\"\x00\x12\x1b\n\tdelete_lb\x12\x03.lb\x1a\x07.result\"\x00\x12\x1f\n\x0b\x64\x65lete_kube\x12\x05.kube\x1a\x07.result\"\x00\x12\x1f\n\x0b\x64\x65lete_plan\x12\x05.plan\x1a\x07.result\"\x00\x12%\n\x0e\x64\x65lete_profile\x12\x08.profile\x1a\x07.result\"\x00\x12\x1f\n\x0b\x64\x65lete_repo\x12\x05.repo\x1a\x07.result\"\x00\x12,\n\x0flist_containers\x12\x06.empty\x1a\x0f.containerslist\"\x00\x12.\n\x15list_container_images\x12\x06.empty\x1a\x0b.imageslist\"\x00\x12$\n\nlist_hosts\x12\x06.empty\x1a\x0c.clientslist\"\x00\x12(\n\rlist_keywords\x12\x06.empty\x1a\r.keywordslist\"\x00\x12\"\n\nlist_kubes\x12\x06.empty\x1a\n.kubeslist\"\x00\x12\x1e\n\x08list_lbs\x12\x06.empty\x1a\x08.lbslist\"\x00\x12\"\n\nlist_plans\x12\x06.empty\x1a\n.planslist\"\x00\x12(\n\rlist_profiles\x12\x06.empty\x1a\r.profileslist\"\x00\x12*\n\rlist_products\x12\x08.product\x1a\r.productslist\"\x00\x12\"\n\nlist_repos\x12\x06.empty\x1a\n.reposlist\"\x00\x12*\n\x11restart_container\x12\n.container\x1a\x07.result\"\x00\x12(\n\x0fstart_container\x12\n.container\x1a\x07.result\"\x00\x12\'\n\x0estop_container\x12\n.container\x1a\x07.result\"\x00\x12\"\n\x0e\x61utostart_plan\x12\x05.plan\x1a\x07.result\"\x00\x12$\n\x10noautostart_plan\x12\x05.plan\x1a\x07.result\"\x00\x12\x1e\n\nstart_plan\x12\x05.plan\x1a\x07.result\"\x00\x12\x1d\n\tstop_plan\x12\x05.plan\x1a\x07.result\"\x00\x12!\n\x0bswitch_host\x12\x07.client\x1a\x07.result\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kcli_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=14
  _EMPTY._serialized_end=21
  _VERSION._serialized_start=23
  _VERSION._serialized_end=70
  _CLIENT._serialized_start=73
  _CLIENT._serialized_end=544
  _CLIENTSLIST._serialized_start=546
  _CLIENTSLIST._serialized_end=585
  _VM._serialized_start=588
  _VM._serialized_end=722
  _SNAPSHOT._serialized_start=724
  _SNAPSHOT._serialized_end=769
  _NETINFO._serialized_start=771
  _NETINFO._serialized_end=836
  _DISKINFO._serialized_start=838
  _DISKINFO._serialized_end=922
  _VMINFO._serialized_start=925
  _VMINFO._serialized_end=1513
  _VMLIST._serialized_start=1515
  _VMLIST._serialized_end=1545
  _RESULT._serialized_start=1547
  _RESULT._serialized_end=1618
  _PROFILE._serialized_start=1621
  _PROFILE._serialized_end=1794
  _PROFILESLIST._serialized_start=1796
  _PROFILESLIST._serialized_end=1838
  _ISOSLIST._serialized_start=1840
  _ISOSLIST._serialized_end=1864
  _IMAGE._serialized_start=1866
  _IMAGE._serialized_end=1888
  _IMAGESLIST._serialized_start=1890
  _IMAGESLIST._serialized_end=1918
  _DISK._serialized_start=1920
  _DISK._serialized_end=1968
  _DISKSLIST._serialized_start=1970
  _DISKSLIST._serialized_end=2003
  _PLAN._serialized_start=2005
  _PLAN._serialized_end=2038
  _PLANSLIST._serialized_start=2040
  _PLANSLIST._serialized_end=2073
  _KEYWORD._serialized_start=2075
  _KEYWORD._serialized_end=2116
  _KEYWORDSLIST._serialized_start=2118
  _KEYWORDSLIST._serialized_end=2160
  _POOL._serialized_start=2162
  _POOL._serialized_end=2242
  _POOLSLIST._serialized_start=2244
  _POOLSLIST._serialized_end=2277
  _NETWORK._serialized_start=2280
  _NETWORK._serialized_end=2436
  _NETWORKSLIST._serialized_start=2438
  _NETWORKSLIST._serialized_end=2480
  _SUBNET._serialized_start=2482
  _SUBNET._serialized_end=2549
  _SUBNETSLIST._serialized_start=2551
  _SUBNETSLIST._serialized_end=2590
  _KUBE._serialized_start=2592
  _KUBE._serialized_end=2639
  _KUBESLIST._serialized_start=2641
  _KUBESLIST._serialized_end=2674
  _LB._serialized_start=2676
  _LB._serialized_end=2753
  _LBSLIST._serialized_start=2755
  _LBSLIST._serialized_end=2782
  _FLAVOR._serialized_start=2784
  _FLAVOR._serialized_end=2841
  _FLAVORSLIST._serialized_start=2843
  _FLAVORSLIST._serialized_end=2882
  _REPO._serialized_start=2884
  _REPO._serialized_end=2917
  _REPOSLIST._serialized_start=2919
  _REPOSLIST._serialized_end=2952
  _PRODUCT._serialized_start=2954
  _PRODUCT._serialized_end=3062
  _PRODUCTSLIST._serialized_start=3064
  _PRODUCTSLIST._serialized_end=3106
  _CONFIG._serialized_start=3108
  _CONFIG._serialized_end=3154
  _CONTAINER._serialized_start=3156
  _CONTAINER._serialized_end=3279
  _CONTAINERSLIST._serialized_start=3281
  _CONTAINERSLIST._serialized_end=3329
  _SSHCMD._serialized_start=3331
  _SSHCMD._serialized_end=3355
  _CMD._serialized_start=3357
  _CMD._serialized_end=3375
  _SCPDETAILS._serialized_start=3377
  _SCPDETAILS._serialized_end=3491
  _VMFILE._serialized_start=3493
  _VMFILE._serialized_end=3534
  _VMPROFILE._serialized_start=3537
  _VMPROFILE._serialized_end=3698
  _KCLI._serialized_start=3701
  _KCLI._serialized_end=4445
  _KCONFIG._serialized_start=4448
  _KCONFIG._serialized_end=5540
# @@protoc_insertion_point(module_scope)