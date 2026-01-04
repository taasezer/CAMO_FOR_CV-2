import { Video, Package, BarChart3, Settings, Search } from "lucide-react";

function App() {
  return (
    <div className="flex h-screen bg-background text-foreground overflow-hidden">
      {/* Sidebar */}
      <aside className="w-64 border-r border-border bg-card hidden md:flex flex-col">
        <div className="p-6 border-b border-border">
          <h1 className="text-xl font-bold tracking-tight text-primary">
            NEXUS<span className="text-blue-500">LOGISTICS</span>
          </h1>
          <p className="text-xs text-muted-foreground mt-1">AI Command Center</p>
        </div>

        <nav className="flex-1 p-4 space-y-2">
          <NavItem icon={<Video />} label="Live Monitor" active />
          <NavItem icon={<Package />} label="Shipments" />
          <NavItem icon={<BarChart3 />} label="Analytics" />
          <NavItem icon={<Settings />} label="System Config" />
        </nav>

        <div className="p-4 border-t border-border">
          <div className="bg-secondary/50 rounded-lg p-3">
            <div className="flex items-center gap-2 mb-2">
              <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
              <span className="text-xs font-medium">System Online</span>
            </div>
            <p className="text-[10px] text-muted-foreground">v2.0.0-alpha</p>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col">
        {/* Header */}
        <header className="h-16 border-b border-border flex items-center justify-between px-6 bg-card/50 backdrop-blur-sm">
          <h2 className="text-lg font-semibold">Mission Control</h2>
          <div className="flex items-center gap-4">
            <div className="relative">
              <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-muted-foreground" />
              <input
                type="text"
                placeholder="Search tracking ID..."
                className="h-9 w-64 rounded-md border border-input bg-background pl-9 pr-3 text-sm focus:outline-none focus:ring-1 focus:ring-ring"
              />
            </div>
          </div>
        </header>

        {/* Dashboard Area */}
        <div className="flex-1 p-6 overflow-auto bg-background/95">
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 h-full">
            {/* Main Video Feed */}
            <div className="lg:col-span-2 flex flex-col gap-6">
              <div className="rounded-xl border border-border bg-black/50 aspect-video relative overflow-hidden group">
                <img
                  src="http://localhost:8000/video/feed"
                  alt="Live Camera"
                  className="w-full h-full object-cover"
                  onError={(e) => {
                    // While backend is offline, show placeholder
                    e.currentTarget.style.display = 'none';
                    e.currentTarget.parentElement!.querySelector('.placeholder')!.classList.remove('hidden');
                  }}
                />
                <div className="placeholder hidden absolute inset-0 flex items-center justify-center flex-col gap-2 text-muted-foreground">
                  <Video className="w-12 h-12 opacity-50" />
                  <p>Connecting to Video Feed...</p>
                </div>

                {/* HUD Overlay */}
                <div className="absolute top-4 left-4 flex gap-2">
                  <span className="px-2 py-1 rounded bg-red-500/80 text-white text-xs font-bold animate-pulse">LIVE</span>
                  <span className="px-2 py-1 rounded bg-black/50 text-white text-xs font-mono">CAM-01</span>
                </div>

                <div className="absolute inset-0 border-2 border-primary/20 pointer-events-none rounded-xl"></div>
              </div>

              {/* Stats Row */}
              <div className="grid grid-cols-3 gap-4">
                <StatCard title="Packages Today" value="124" trend="+12%" />
                <StatCard title="Throughput" value="42/h" trend="+5%" />
                <StatCard title="Pending" value="8" trend="normal" />
              </div>
            </div>

            {/* Side Panel (Logs) */}
            <div className="rounded-xl border border-border bg-card p-4 flex flex-col h-full">
              <h3 className="font-semibold mb-4">Recent Activity</h3>
              <div className="space-y-4 overflow-y-auto flex-1 pr-2">
                {[1, 2, 3, 4, 5].map((i) => (
                  <div key={i} className="flex gap-3 items-start border-b border-border/50 pb-3 last:border-0">
                    <div className="w-8 h-8 rounded-full bg-blue-500/10 flex items-center justify-center text-blue-500 shrink-0">
                      <Package className="w-4 h-4" />
                    </div>
                    <div>
                      <p className="text-sm font-medium">Order #TR-882{i}</p>
                      <p className="text-xs text-muted-foreground">Processed 2 mins ago</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}

function NavItem({ icon, label, active = false }: { icon: any, label: string, active?: boolean }) {
  return (
    <button className={`w-full flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${active ? 'bg-primary/10 text-primary' : 'hover:bg-accent text-muted-foreground hover:text-accent-foreground'}`}>
      {icon}
      {label}
    </button>
  )
}

function StatCard({ title, value, trend }: { title: string, value: string, trend: string }) {
  return (
    <div className="rounded-xl border border-border bg-card p-4">
      <p className="text-xs text-muted-foreground">{title}</p>
      <div className="flex items-end justify-between mt-1">
        <span className="text-2xl font-bold">{value}</span>
        <span className={`text-xs ${trend.includes('+') ? 'text-green-500' : 'text-muted-foreground'}`}>{trend}</span>
      </div>
    </div>
  )
}

export default App;
