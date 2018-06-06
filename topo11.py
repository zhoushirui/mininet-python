from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        host3 = self.addHost( 'h3' )
        host4 = self.addHost( 'h4' )
        host5 = self.addHost( 'h5' )
        host6 = self.addHost( 'h6' )
        host7 = self.addHost( 'h7' )
        host8 = self.addHost( 'h8' )
        switch1 = self.addSwitch( 's1' )
        switch2 = self.addSwitch( 's2' )
        switch3 = self.addSwitch( 's3' )
        switch4 = self.addSwitch( 's4' )
        switch5 = self.addSwitch( 's5' )
        switch6 = self.addSwitch( 's6' )
        switch7 = self.addSwitch( 's7' )

        # Add links
        self.addLink( switch1,switch2,1,1)
        self.addLink( switch1,switch3,2,1)
        self.addLink( switch2,switch4,2,1)
        self.addLink( switch2,switch5,3,1)
        self.addLink( switch3,switch6,2,1)
        self.addLink( switch3,switch7,3,1)
        self.addLink( switch4,host1,2,1)
        self.addLink( switch4,host2,3,1)
        self.addLink( switch5,host3,2,1)
        self.addLink( switch5,host4,3,1)
        self.addLink( switch6,host5,2,1)
        self.addLink( switch6,host6,3,1)
        self.addLink( switch7,host7,2,1)
        self.addLink( switch7,host8,3,1)

topos = { 'mytopo': ( lambda: MyTopo() ) }
