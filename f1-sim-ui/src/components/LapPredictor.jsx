import React, { useState } from 'react';
import axios from 'axios';
import { motion } from 'framer-motion';

const LapPredictor = () => {
  const [form, setForm] = useState({ driver: '', year: '', circuit: '', compound: '' });
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    try {
      const res = await axios.get(`https://f1-sim-backend.onrender.com/`, {
        params: form
      });
      setResult(res.data);
    } catch (err) {
      alert("Error fetching prediction");
    }
  };

  return (
    <section id="lap-predictor" className="min-h-screen p-8 bg-zinc-900">
      <motion.div
        initial={{ opacity: 0 }}
        whileInView={{ opacity: 1 }}
        transition={{ duration: 1 }}
        className="max-w-3xl mx-auto text-center"
      >
        <h2 className="text-4xl text-red-400 font-semibold mb-6">Lap Time Predictor</h2>
        <div className="space-y-4">
          {['driver', 'year', 'circuit', 'compound'].map((field) => (
            <input
              key={field}
              name={field}
              placeholder={field}
              value={form[field]}
              onChange={handleChange}
              className="w-full px-4 py-2 bg-black border border-gray-700 rounded text-white"
            />
          ))}
          <button onClick={handleSubmit} className="mt-4 px-6 py-2 bg-red-600 rounded hover:bg-red-700">
            Predict Lap Time
          </button>
        </div>
        {result && (
          <div className="mt-6 text-lg">
            <p><strong>Predicted Time:</strong> {result.predicted_lap_time_formatted}</p>
            <p><strong>In Seconds:</strong> {result.predicted_lap_time_seconds}</p>
          </div>
        )}
      </motion.div>
    </section>
  );
};

export default LapPredictor;
