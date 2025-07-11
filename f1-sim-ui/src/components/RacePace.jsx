import React, { useState } from 'react';
import axios from 'axios';
import { motion } from 'framer-motion';

const RacePace = () => {
  const [form, setForm] = useState({ driver: '', year: '', circuit: '', compound: '', laps: 50 });
  const [lapTimes, setLapTimes] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const simulateRace = async () => {
    try {
      const res = await axios.get(`https://f1-sim-backend.onrender.com/predict/race_pace`, {
        params: form
      });
      setLapTimes(res.data);
    } catch (err) {
      alert("Error simulating race pace");
    }
  };

  return (
    <section className="min-h-screen p-8 bg-black text-white">
      <motion.div initial={{ opacity: 0 }} whileInView={{ opacity: 1 }} transition={{ duration: 1 }} className="max-w-4xl mx-auto text-center">
        <h2 className="text-4xl font-bold text-yellow-400 mb-6">Race Pace Simulation</h2>

        <div className="grid grid-cols-2 gap-4 mb-6">
          {['driver', 'year', 'circuit', 'compound', 'laps'].map((field) => (
            <input
              key={field}
              name={field}
              placeholder={field}
              value={form[field]}
              onChange={handleChange}
              className="px-4 py-2 bg-zinc-800 border border-gray-700 rounded"
            />
          ))}
        </div>
        <button onClick={simulateRace} className="px-6 py-2 bg-yellow-500 text-black rounded hover:bg-yellow-600">
          Simulate Race
        </button>

        {lapTimes && (
          <div className="mt-6 text-left bg-zinc-800 p-4 rounded">
            <h3 className="text-xl font-bold mb-2">Total Race Time: {lapTimes.total_race_time}</h3>
            <div className="overflow-y-auto h-64">
              <ol className="list-decimal ml-6 space-y-1">
                {lapTimes.lap_times.map((t, idx) => (
                  <li key={idx}>Lap {idx + 1}: {t}</li>
                ))}
              </ol>
            </div>
          </div>
        )}
      </motion.div>
    </section>
  );
};

export default RacePace;