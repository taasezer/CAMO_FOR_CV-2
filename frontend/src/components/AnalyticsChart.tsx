import { useEffect, useState } from 'react';
import axios from 'axios';
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

export function AnalyticsChart() {
    const [data, setData] = useState([]);

    useEffect(() => {
        // Initial fetch
        fetchData();

        // Refresh every 30s
        const interval = setInterval(fetchData, 30000);
        return () => clearInterval(interval);
    }, []);

    const fetchData = () => {
        axios.get('http://localhost:8000/analytics/activity-graph')
            .then(res => setData(res.data))
            .catch(err => console.error(err));
    };

    return (
        <div className="h-[200px] w-full mt-4 bg-card border border-border rounded-xl p-4">
            <h3 className="text-sm font-semibold mb-4 text-muted-foreground">Hourly Throughput</h3>
            <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={data}>
                    <defs>
                        <linearGradient id="colorPackages" x1="0" y1="0" x2="0" y2="1">
                            <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3} />
                            <stop offset="95%" stopColor="#3b82f6" stopOpacity={0} />
                        </linearGradient>
                    </defs>
                    <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#333" />
                    <XAxis
                        dataKey="time"
                        tick={{ fontSize: 12, fill: '#666' }}
                        axisLine={false}
                        tickLine={false}
                    />
                    <YAxis
                        tick={{ fontSize: 12, fill: '#666' }}
                        axisLine={false}
                        tickLine={false}
                    />
                    <Tooltip
                        contentStyle={{ backgroundColor: '#1a1a1a', border: '1px solid #333' }}
                        itemStyle={{ color: '#fff' }}
                    />
                    <Area
                        type="monotone"
                        dataKey="packages"
                        stroke="#3b82f6"
                        strokeWidth={2}
                        fillOpacity={1}
                        fill="url(#colorPackages)"
                    />
                </AreaChart>
            </ResponsiveContainer>
        </div>
    );
}
