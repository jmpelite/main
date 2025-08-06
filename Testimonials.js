import React from 'react';

const Testimonials = () => {
  const testimonials = [
    {
      text: "I finally started feeling confident—without changing my social life. JMP gets it, no lectures.",
      name: "Steph",
      age: "25",
      location: "Glasgow"
    },
    {
      text: "Always honest, never judgy. Best advice for balancing parties and progress.",
      name: "Calum",
      age: "22",
      location: "Dundee"
    },
    {
      text: "After working with JMP, my sleep and mood are up, and I don't feel guilty about nights out.",
      name: "Megan",
      age: "19",
      location: "Edinburgh"
    },
    {
      text: "Finally found someone who understands student life. Real advice that actually works.",
      name: "Jamie",
      age: "21",
      location: "Stirling"
    }
  ];

  return (
    <section id="testimonials" className="max-w-7xl mx-auto px-4 py-16">
      <div className="bg-gray-800 rounded-2xl shadow-2xl p-8 md:p-12">
        <h2 className="text-3xl md:text-4xl font-bold text-blue-400 mb-8 text-center">Real Results, Real People</h2>
        <div className="grid gap-6 md:grid-cols-2">
          {testimonials.map((testimonial, index) => (
            <div key={index} className="bg-gray-700 rounded-xl p-6 card-hover border-l-4 border-blue-400">
              <p className="text-gray-300 leading-relaxed mb-4 italic text-lg">
                "{testimonial.text}"
              </p>
              <div className="text-blue-300 font-semibold">
                – {testimonial.name}, {testimonial.age}, {testimonial.location}
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Testimonials;