"""Custom topology example
Two directly connected switches plus a host for each switch:
host --- switch --- switch --- host
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""
from mininet.topo import Topo
class MyTopo( Topo ):
"Simple topology example."
def __init__( self ):
"Create custom topo."
# Initialize topology
Topo.__init__( self )
# Add hosts and switches
H1 = self.addHost('h1')
H2 = self.addHost('h2')
H3 = self.addHost('h3')
H4 = self.addHost('h4')
H5 = self.addHost('h5')
H6 = self.addHost('h6')
H7 = self.addHost('h7')
H8 = self.addHost('h8')
H9 = self.addHost('h9')
H10 = self.addHost('h10')
S1 = self.addSwitch('s1')
S2 = self.addSwitch('s2')
S3 = self.addSwitch('s3')
S4 = self.addSwitch('s4')
switchList = (S1,S2,S3,S4)
# Add links
for i in range(0,len(switchList))
	for j in range(i+1,len(switchList))
		self.addLink(switchList[i],switchList[j])
self.addLink(H1,S1)
self.addLink(H2,S1)
self.addLink(H3,S1)
self.addLink(H4,S1)
self.addLink(H5,S1)
self.addLink(H6,S3)
self.addLink(H7,S3)
self.addLink(H8,S3)
self.addLink(H9,S3)
self.addLink(H10,S3)
topos = { 'mytopo': ( lambda: MyTopo() ) }
