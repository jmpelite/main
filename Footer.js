import React from 'react';

const Footer = () => {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-gray-900 border-t border-gray-800 py-8">
      <div className="max-w-7xl mx-auto px-4 text-center">
        <div className="mb-4">
          <h3 className="text-xl font-bold text-blue-400 mb-2">JMP Coaching</h3>
          <p className="text-gray-300">Real fitness for real life</p>
        </div>

        <div className="flex justify-center space-x-6 mb-4">
          <a href="#about" className="text-gray-400 hover:text-blue-400 transition-colors">About</a>
          <a href="#credentials" className="text-gray-400 hover:text-blue-400 transition-colors">Qualifications</a>
          <a href="#tips" className="text-gray-400 hover:text-blue-400 transition-colors">Tips</a>
          <a href="#contact" className="text-gray-400 hover:text-blue-400 transition-colors">Contact</a>
        </div>

        <div className="text-gray-500 text-sm">
          <p>&copy; {currentYear} JMP Coaching. All rights reserved.</p>
          <p className="mt-2">
            Qualified Personal Trainer & Nutrition Specialist | Mental Health Aware
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;