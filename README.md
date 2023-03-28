### Merton Probability of Default Calculator

#### Miguel C. Herculano, University of Glasgow, January 2018

#### ------------------------------------------------------------------------------------------------------------------------------------------------------------
#### Instructions:

To install run the following command which will pull and install the latest commit from this repository, along with its Python dependencies:

```python
pip install git+https://github.com/mcherculano/merton_pds.git
```

Add the following line to your .py script: 

```python
import merton_pds.merton_pds as pds
```
#### ----------------------------------------------------------------------------------------------------------------------------------------------------------
##### Required Inputs:
- Equity: Market value of the firm's equity.
- Liabilities: Liability threshold of the firm.
- Rate: Risk-free interest rate
- **kwargs: 
    - 'Maturity': default is 1, should be consistent with implied assumption on maturity of default threshold (liabilities)
    - 'Drift': default is 'rate' 
    - 'NumPeriods': typically number of trading periods in a year. default 255
    - 'Tolerance': Used by the Solver. default is 1e-6)
    - 'MaxIterations' Used by the Solver. default is 500


#### ----------------------------------------------------------------------------------------------------------------------------------------------------------
#### Theory:
This program calculates Probabilities of Default for a a set of N firms across a number of time periods T.

The market value of the firm’s underlying assets $Va$ follows the stochastic process:

$$dVa = \mu *Va *dt + \sigma *Va *dz$$ 

If X is the book value, then

$$ Ve = Va *N(d1) - exp(-rT) *X *N(d2) $$

where Ve is the market value of the firm’s equity, and

$$ d1 = [ln(Va/X) + (r+\sigma^2/2)T ]/ [\sigma*\sqrt{T}] $$

$$ d2 = d1 - \sigma*\sqrt{T} $$

where $r$ is the risk-free interest rate. Thus,

 $$ PD = N [(ln(Va/X)+( \mu -\sigma^2) *T)/(\sigma *\sqrt{2})] $$
 
#### ------------------------------------------------------------------------------------------------------------------------------------------------------------
#### Notes:

- This can be done for any quoted firm. As an example this code draws on a random set of US banks. Data sourced from Datastream.
- Default threshold defined as current liabilities (short-term debt plus current portion of long-term debt) (see References).

#### ------------------------------------------------------------------------------------------------------------------------------------------------------------
#### REFERENCES:

[1] Gray, D. F., Merton, R. C., and Bodie, Z. (2007). Framework for Measuring and Managing Macrofinancial Risk and Financial. NBER Working Paper Series, pages 1{32}.

[2] Gupton, G. M., Finger, C. C., and Bhatia, M. (2007). CreditMetrics - Technical Document.

[3] Crosbie,P.J. and Bohn,J.R. (2003) "Modeling Default Risk", available online: http://www.defaultrisk.com/pp_model_35.htm

#### ------------------------------------------------------------------------------------------------------------------------------------------------------------


