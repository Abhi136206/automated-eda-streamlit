import { Card, CardContent } from "@/components/ui/card";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, BarChart, Bar } from "recharts";
import { useState } from "react";
import { Button } from "@/components/ui/button";

const data = [
  { month: "Jan", revenue: 4000, users: 2400, engagement: 80 },
  { month: "Feb", revenue: 3000, users: 1398, engagement: 70 },
  { month: "Mar", revenue: 5000, users: 2800, engagement: 85 },
  { month: "Apr", revenue: 7000, users: 3900, engagement: 90 },
  { month: "May", revenue: 6000, users: 3500, engagement: 88 },
  { month: "Jun", revenue: 8000, users: 4600, engagement: 95 },
];

export default function Dashboard() {
  const [metric, setMetric] = useState("revenue");

  return (
    <div className="p-6 grid grid-cols-1 md:grid-cols-2 gap-6">
      {/* Line Chart Card */}
      <Card>
        <CardContent>
          <h2 className="text-xl font-semibold mb-4">Performance Overview</h2>
          <div className="flex gap-4 mb-4">
            <Button onClick={() => setMetric("revenue")} variant="outline">Revenue</Button>
            <Button onClick={() => setMetric("users")} variant="outline">Users</Button>
            <Button onClick={() => setMetric("engagement")} variant="outline">Engagement</Button>
          </div>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={data}>
              <XAxis dataKey="month" />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey={metric} stroke="#8884d8" strokeWidth={2} />
            </LineChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>

      {/* Bar Chart Card */}
      <Card>
        <CardContent>
          <h2 className="text-xl font-semibold mb-4">User Engagement Analysis</h2>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={data}>
              <XAxis dataKey="month" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="engagement" fill="#82ca9d" />
            </BarChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>
    </div>
  );
}
