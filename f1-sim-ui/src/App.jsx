import React from 'react';
import { motion } from 'framer-motion';
import Hero from './components/Hero';
import LapPredictor from './components/LapPredictor';
import RacePace from './components/RacePace';
import HowItWorks from './components/HowItWorks';
import Footer from './components/Footer';

const App = () => {
  return (
    <div className="bg-black text-white font-orbitron scroll-smooth">
      <Hero />
      <LapPredictor />
      <RacePace />
      <HowItWorks />
      <Footer />
    </div>
  );
};

export default App;
