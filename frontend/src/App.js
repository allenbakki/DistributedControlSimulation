import { useEffect, useState } from "react";
import axios from "axios";
import { Card, Table } from "antd";
import { LineChart, Line, XAxis, YAxis, Tooltip, Legend } from "recharts";

export default function App() {
  const [state, setState] = useState({});
  const [history, setHistory] = useState([]);

  useEffect(() => {
    const interval = setInterval(() => {
      axios
        .get("http://127.0.0.1:5000/state")
        .then(res => {
          setState(res.data);
          setHistory(h => [
            ...h,
            {
              time: new Date(res.data.timestamp * 1000).toLocaleTimeString(),
              speed: res.data.speed,
            },
          ]);
        })
        .catch(err => console.log("Backend not reachable", err));
    }, 500);

    return () => clearInterval(interval);
  }, []);

  const tableColumns = [{ title: "Value", dataIndex: "value", key: "value" }];

  return (
    <div style={{ padding: 20, maxWidth: 800, margin: "0 auto" }}>
      {/* Plant Current State */}
      <Card title="Plant Current State" style={{ marginBottom: 20 }}>
        <p>
          <b>Speed:</b> {state.speed?.toFixed(2)}
        </p>
        <p>
          <b>Target:</b> {state.target}
        </p>
      </Card>

      {/* Controller Inputs Table */}
      <Card
        title="Controller Inputs"
        style={{ marginBottom: 20, maxWidth: "100%", overflowX: "auto" }}
      >
        <div style={{ maxHeight: 200, overflowY: "auto" }}>
          <Table
            dataSource={state.controller_inputs?.map((v, i) => ({
              key: i,
              value: v.toFixed(2),
            }))}
            columns={tableColumns}
            pagination={false}
            scroll={{ x: "max-content" }}
          />
        </div>
      </Card>

      {/* Speed Over Time Chart */}
      <Card title="Speed Over Time">
        <LineChart width={700} height={350} data={history}>
          <Line type="monotone" dataKey="speed" stroke="#ff0000" name="Speed" />
          <XAxis dataKey="time" />
          <YAxis />
          <Tooltip />
          <Legend verticalAlign="top" height={36} />
        </LineChart>
      </Card>
    </div>
  );
}
