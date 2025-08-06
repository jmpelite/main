import React from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import About from './components/About';
import Credentials from './components/Credentials';
import Tips from './components/Tips';
import Testimonials from './components/Testimonials';
import Contact from './components/Contact';
import Footer from './components/Footer';
import './App.css';

function App() {
  return (
    <div className="bg-gray-900 text-gray-100 min-h-screen">
      <Header />
      <main>
        <Hero />
        <About />
        <Credentials />
        <Tips />
        <Testimonials />
        <Contact />
      </main>
      <Footer />
    </div>
  );
}

export default App;