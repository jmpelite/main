import React from 'react';

const About = () => (
  <section id="about" className="max-w-5xl mx-auto px-4 py-16">
    <div className="bg-gray-800 rounded-2xl shadow-2xl p-8 md:p-12 card-hover">
      <h2 className="text-3xl md:text-4xl font-bold text-blue-400 mb-6">Why I Get It</h2>
      <div className="text-gray-300 leading-relaxed text-lg space-y-4">
        <p>
          Fitness shouldn't mean giving up what makes life fun. I've trained, coached, and lived it—from Friday club nights to Sunday gym sessions.
        </p>
        <p>
          I help you balance social life, nightlife, and health—so you feel great in and out of the gym. <strong>No judgment, just honest support.</strong>
        </p>
        <p className="text-blue-300 font-semibold">
          Real experience. Real results. Real life.
        </p>
      </div>
    </div>
  </section>
);

export default About;