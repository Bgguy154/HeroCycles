1. What is the most important thing on the configurator screen?

The price breakdown and final total are the most important elements on the configurator screen. They are displayed prominently at the bottom of the interface using clear formatting and larger typography so the salesperson can quickly verify the final quote and ensure it matches the selected parts.

2. What did you do to make repetitive use fast and easy?
Default values:
The date field is prefilled (2016-12-15), and commonly used parts are selected by default. This allows the salesperson to generate a quote immediately for standard configurations with minimal interaction.
Single-click updates:
The UI updates the pricing breakdown only when the user clicks the “Calculate Price” button, rather than recalculating after every dropdown change. This reduces unnecessary visual noise and makes rapid configuration smoother and more efficient.
3. What happens when a part combination is invalid?

In this prototype, all part combinations are currently accepted because the pricing engine simply sums the prices of selected parts independently.

In a production-ready system, compatibility validation rules would be added. For example, a tubeless tyre would only be allowed with a compatible rim. If the user selects incompatible parts, the interface would display a clear warning banner above the pricing output, explaining which combination is invalid and why.

4. One thing you would improve if you had more time

I would integrate the frontend with a backend pricing engine, such as a Python/Flask /price API or a Node.js service. This would allow:

The frontend to send date and part_ids as JSON payloads.
The backend to calculate time-sensitive pricing dynamically and return a detailed price breakdown.