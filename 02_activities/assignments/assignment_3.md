# Data Visualization

## Assignment 3: Final Project

### Requirements:
- We will finish this class by giving you the chance to use what you have learned in a practical context, by creating data visualizations from raw data. 
- Choose a dataset of interest from the [City of Toronto’s Open Data Portal](https://www.toronto.ca/city-government/data-research-maps/open-data/) or [Ontario’s Open Data Catalogue](https://data.ontario.ca/). 
- Using Python and one other data visualization software (Excel or free alternative, Tableau Public, any other tool you prefer), create two distinct visualizations from your dataset of choice.  

- For each visualization, describe and justify: 
    > What software did you use to create your data visualization?
   -  For this project, I used Python (Matplotlib and Seaborn) to create the initial bar chart and Google Sheets to design a time series plot. 

    > Who is your intended audience? 
    - The intended audience are city planners, art enthusiasts, and community members interested in understanding the distribution and growth of public art installations over time in Toronto.
    
    > What information or message are you trying to convey with your visualization? 
   -  Both visualizations aim to show how public art installations have evolved over the years and to highlight the diversity of art forms present in the city. 
    1. The bar chart reveals which types of artworks are most prevalent. 
    2. The time series chart illustrates trends in installation activity, potentially reflecting cultural shifts or policy changes.

    
    > What design principles (substantive, perceptual, aesthetic) did you consider when making your visualization? How did you apply these principles? With what elements of your plots? 
    - I selected data points that reveal meaningful patterns, such as the frequency of different art forms and the number of installations per year. 
    - I used distinct colors and clear labeling to ensure viewers can quickly grasp key insights. 
    - In the bar chart, the art forms are listed along the x-axis, with counts on the y-axis, making comparisons straightforward. 
    - Finally, I chose color palettes that enhance readability and adjusted label angles in Google Sheets to prevent overlap, ensuring a clean, visually balanced design.

    
    > How did you ensure that your data visualizations are reproducible? If the tool you used to make your data visualization is not reproducible, how will this impact your data visualization? 
   -  The Python visualizations are fully reproducible with the script provided, and the time series data is exported as a CSV for easy replication in tools like Google Sheets, Excel or Tableau.

    
    > How did you ensure that your data visualization is accessible?  
   -  I prioritized accessibility by ensuring all labels, titles, and legends are clear and legible. I also tried choosing colorblind-friendly palettes.

    
    > Who are the individuals and communities who might be impacted by your visualization?  
   -  These visualizations can impact local artists, city planners, and residents by highlighting identifying periods of growth and decline in public art funding and types of art forms that are most prevalent. 

    
    > How did you choose which features of your chosen dataset to include or exclude from your visualization? 
    - I focused on the art form and installation year as key features, as these dimensions offer both, an understanding of the available art forms, and insights into changes over time. To avoid the visualizations being less cluttered, less relevant attributes were excluded.

    
    > What ‘underwater labour’ contributed to your final data visualization product?
    - The project involved reformatting column labels for compatibility with the chosen visualization tools and refining design choices to ensure a balance between detail and clarity.


- This assignment is intentionally open-ended - you are free to create static or dynamic data visualizations, maps, or whatever form of data visualization you think best communicates your information to your audience of choice! 
- Total word count should not exceed **(as a maximum) 1000 words** 
 
### Why am I doing this assignment?:  
- This ongoing assignment ensures active participation in the course, and assesses the learning outcomes: 
* Create and customize data visualizations from start to finish in Python
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story  
- This would be a great project to include in your GitHub Portfolio – put in the effort to make it something worthy of showing prospective employers!

### Rubric:

| Component         | Scoring  | Requirement                                                                 |
|-------------------|----------|-----------------------------------------------------------------------------|
| Data Visualizations | Complete/Incomplete | - Data visualizations are distinct from each other<br>- Data visualizations are clearly identified<br>- Different sources/rationales (text with two images of data, if visualizations are labeled)<br>- High-quality visuals (high resolution and clear data)<br>- Data visualizations follow best practices of accessibility |
| Written Explanations | Complete/Incomplete | - All questions from assignment description are answered for each visualization<br>- Explanations are supported by course content or scholarly sources, where needed |
| Code              | Complete/Incomplete | - All code is included as an appendix with your final submissions<br>- Code is clearly commented and reproducible |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 09/03/2025`
* The branch name for your repo should be: `assignment-4`
* What to submit for this assignment:
    * A folder/directory containing:
        * This file (assignment_3.md)
        * Two data visualizations 
        * Two markdown files for each both visualizations with their written descriptions.
        * Link to your dataset of choice.
        * Complete and commented code as an appendix (for your visualization made with Python, and for the other, if relevant) 
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-3`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
