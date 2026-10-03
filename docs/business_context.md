# Business Context

## Problem

Banks need reliable methods to assess customer credit risk. Traditional credit assessment can be complemented by additional customer and banking attributes.

## Objective

Build and compare classification models that predict the observed `DefaulterYN` outcome.

## Stakeholders

| Stakeholder | Business question |
|---|---|
| Credit / Risk Team | Which customers may require additional review? |
| Lending Team | How can risk signals support existing policy? |
| Model Risk Team | How reliable and stable is the model? |
| Management | What trade-offs exist between missed defaults and false alerts? |

## Success Criteria

The model should not be evaluated on accuracy alone. Recall, precision, F1 and confusion matrices should be considered together, with the business cost of false positives and false negatives explicitly defined before threshold selection.
