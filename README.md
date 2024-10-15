# Script-Agnostic Language Identification

	


# Summary

 :mega:	**Motivation**: Language identification is used as the first step in many data collection and crawling efforts because it allows us to sort online text into language-specific buckets. However, many modern languages, such as Konkani, Kashmiri, Punjabi etc., are **synchronically written** in several scripts. Moreover, languages with different writing systems do not share significant lexical, semantic, and syntactic properties in neural representation spaces, which is a disadvantage for closely related languages and low-resource languages, especially those from the Indian Subcontinent. 

To counter this, we propose learning script-agnostic representations using several different experimental strategies.

:pushpin:	Sentence-Level Upscaling

:pushpin:	Script Projection/Flattening

:pushpin:	Intra-Sentence Mixing

We focus our proof-of-concept study on four major Dravidian languages (Tamil, Telugu, Kannada, and Malayalam). 

 :mega:**Finding**: We find that word-level script randomization and exposure to a language written in multiple scripts is extremely valuable for downstream script-agnostic language identification, while also maintaining competitive performance on naturally occurring text.

# Poster
This work was recently presented at SouthNLP 2024 at Emory University and MASC-SLL 2024 at Johns Hopkins University (Best Paper Award). The poster is also [available in the repository](poster.pdf) for a visual overview 
<!--
# Code
This repository contains all the scripts we used to download, generate, preprocess, and evaluate the data and models. It is not organized in a  pipeline manner as each script has its function, but the functions are modularized as much as possible so you can reuse the relevant scripts for replicating certain experiments or for your own use.

## Cite This Project
We will add a link to the arXiv identifier below soon.
```
@misc{agarwal2024-salid,
      title={Script-Agnostic Language Identification}, 
      author={Milind Agarwal and Joshua Otten and Antonios Anastasopoulos},
      year={2024},
      eprint={ },
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
-->
