# Create final React components

# Contact component
contact_js = """import React, { useState } from 'react';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Create mailto link with form data
    const subject = encodeURIComponent('Coaching Enquiry from ' + formData.name);
    const body = encodeURIComponent(`Name: ${formData.name}\\nEmail: ${formData.email}\\n\\nMessage:\\n${formData.message}`);
    const mailtoLink = `mailto:hello@jmpcoaching.com?subject=${subject}&body=${body}`;
    window.location.href = mailtoLink;
  };

  return (
    <section id="contact" className="max-w-5xl mx-auto px-4 py-16">
      <div className="bg-gray-800 rounded-2xl shadow-2xl p-8 md:p-12">
        <h2 className="text-3xl md:text-4xl font-bold text-blue-400 mb-6 text-center">Get In Touch</h2>
        <p className="text-gray-300 text-lg text-center mb-8 max-w-2xl mx-auto">
          Fast, no-pressure chat. DM me on Instagram, WhatsApp, or fill out the form below for a free consultation.
        </p>

        {/* Contact Options */}
        <div className="grid gap-6 md:grid-cols-3 mb-8">
          <a 
            href="https://instagram.com/yourhandle" 
            target="_blank" 
            rel="noopener noreferrer"
            className="flex items-center justify-center p-4 bg-gradient-to-r from-purple-600 to-pink-600 rounded-lg hover:shadow-lg transition-all duration-300 card-hover"
          >
            <span className="text-white font-semibold text-lg">📱 Instagram DM</span>
          </a>
          <a 
            href="https://wa.me/447123456789" 
            target="_blank" 
            rel="noopener noreferrer"
            className="flex items-center justify-center p-4 bg-green-600 rounded-lg hover:shadow-lg transition-all duration-300 card-hover"
          >
            <span className="text-white font-semibold text-lg">💬 WhatsApp</span>
          </a>
          <button
            onClick={() => document.querySelector('#contact-form').scrollIntoView({ behavior: 'smooth' })}
            className="flex items-center justify-center p-4 bg-blue-600 rounded-lg hover:shadow-lg transition-all duration-300 card-hover"
          >
            <span className="text-white font-semibold text-lg">✉️ Email Form</span>
          </button>
        </div>

        {/* Contact Form */}
        <div id="contact-form" className="max-w-2xl mx-auto">
          <form onSubmit={handleSubmit} className="space-y-6">
            <div>
              <label htmlFor="name" className="block text-gray-300 font-medium mb-2">Name</label>
              <input
                type="text"
                id="name"
                name="name"
                value={formData.name}
                onChange={handleChange}
                required
                className="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:border-blue-400 text-white"
                placeholder="Your name"
              />
            </div>
            <div>
              <label htmlFor="email" className="block text-gray-300 font-medium mb-2">Email</label>
              <input
                type="email"
                id="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
                className="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:border-blue-400 text-white"
                placeholder="your.email@example.com"
              />
            </div>
            <div>
              <label htmlFor="message" className="block text-gray-300 font-medium mb-2">Message</label>
              <textarea
                id="message"
                name="message"
                value={formData.message}
                onChange={handleChange}
                required
                rows="5"
                className="w-full px-4 py-3 bg-gray-700 border border-gray-600 rounded-lg focus:outline-none focus:border-blue-400 text-white resize-vertical"
                placeholder="Tell me about your goals and current situation..."
              ></textarea>
            </div>
            <button
              type="submit"
              className="w-full cta-button bg-blue-600 hover:bg-blue-700 text-white font-bold py-4 px-8 rounded-lg shadow-lg transition-all duration-300 text-lg"
            >
              Send Message →
            </button>
          </form>
        </div>

        {/* Disclaimer */}
        <div className="mt-8 pt-6 border-t border-gray-700">
          <p className="text-gray-400 text-sm text-center">
            <strong>Important:</strong> This is not therapy or medical care. For mental health support, visit 
            <a href="https://www.nhs.uk/mental-health/" target="_blank" rel="noopener noreferrer" className="text-blue-400 hover:text-blue-300 ml-1">NHS Mental Health</a> or 
            <a href="https://www.samaritans.org/" target="_blank" rel="noopener noreferrer" className="text-blue-400 hover:text-blue-300 ml-1">Samaritans (116 123)</a>
          </p>
        </div>
      </div>
    </section>
  );
};

export default Contact;"""

# Footer component
footer_js = """import React from 'react';

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

export default Footer;"""

# Save the final components
with open('Contact.js', 'w') as f:
    f.write(contact_js)

with open('Footer.js', 'w') as f:
    f.write(footer_js)

print("Contact and Footer components created!")