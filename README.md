# Terminal Behavior Analytics
This box is a proof of concept experiment to show how you can run analytics on student reminal use to get a sense of their engagement with the material.

## What does this measure?
The idea is to roughly categorize student behavior into 3 buckets (minimalist, satisficer and explorer) with the following categorizations. 
1. The **minimalist** does less then is asked in the directions - often skipping optional exploration sections.
1. The **satisficer** does approximately what is asked, with negligable variance.
1. The **explorer** does more then is asked in the directions - often digging into the optional exploration sections.

To determine the behvior classification, we compare student terminal command history to what is asked in the assingment (specified in a corresponding file).
An arbitrary threshold is set and later refined in post-hoc analysis.

## What are the assumptions of this approach?
One assumption is the content is rich enough to explore and go beyond following step by step instructions.
Another is that the content invloves considerable use of the terminal to run commands. Commands hidden by buttons are still captured.