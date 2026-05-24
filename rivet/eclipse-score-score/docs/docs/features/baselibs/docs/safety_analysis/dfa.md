---
id: DOC-DFA-22146
title: Dfa
type: specification
status: approved
tags: [eclipse-score]
---

# DFA (Dependent Failure Analysis)

### Baselibs DFA

{{artifact:DOC__BASELIBS_DFA:status,safety-level,security}}

## Dependent Failure Initiators

The DFA for the feature baselibs is performed. To show evidence that all failure initiators are considered, the applicability has to be filled out in the
following tables. For all applicable failure initiators, the DFA has to be performed.

## Dependent Failure Initiators

#### Shared resources

.. list-table:: DFA shared resources (used for Platform DFA)
  :header-rows: 1
  :widths: 10,20,10,20

  * - ID
    - Violation cause shared resources
    - Applicability
    - Rationale
  * - SR_01_01
    - Reused software modules
    - no
    - Baselibs only uses libraries and not other executable modules.
  * - SR_01_02
    - Libraries
    - yes
    - Baselibs filesystem component may suffer from concurrent access to a file, [[FEAT_SAF_DFA__BASELIBS__CONC_FILE_ACCESS]]
  * - SR_01_04
    - Basic software
    - no
    - Not a baselibs specific topic, covered on platform level.
  * - SR_01_05
    - Operating system including scheduler
    - no
    - Not a baselibs specific topic, covered on platform level.
  * - SR_01_06
    - Any service stack, e.g. communication stack
    - no
    - Not a baselibs specific topic, covered on platform level.
  * - SR_01_07
    - Configuration data
    - no
    - No shared configuration data for baselibs.
  * - SR_01_09
    - Execution time
    - no
    - Not a baselibs specific topic, covered on platform level.
  * - SR_01_10
    - Allocated memory
    - yes
    - Bitmanipulation component may operate on the same memory, [[FEAT_SAF_DFA__BASELIBS__CONC_MEMORY_ACCESS]]

#### Communication between the two elements

Receiving function is affected by information that is false, lost, sent multiple times, or in the wrong order etc. from the sender.

.. list-table:: DFA communication between elements
  :header-rows: 1
  :widths: 10,20,10,20

  * - ID
    - Violation cause communication between elements
    - Applicability
    - Rationale
  * - CO_01_01
    - Information passed via argument through a function call, or via writing/reading a variable being global to the two software functions (data flow)
    - no
    - According to its architecture shown in [[FEAT_ARC_STA__BASELIBS__STATIC_VIEW_ARCH]] baselibs do not rely on common input.
  * - CO_01_02
    - Data or message corruption / repetition / loss / delay / masquerading or incorrect addressing of information
    - no
    - Baselibs are not sending messages between their components.
  * - CO_01_03
    - Insertion / sequence of information
    - no
    - Baselibs are not sending messages between their components.
  * - CO_01_04
    - Corruption of information, inconsistent data
    - no
    - Baselibs are not sending messages between their components. Data eventually shared by function calls are covered by FMEA already.
  * - CO_01_05
    - Asymmetric information sent from a sender to multiple receivers, so that not all defined receivers have the same information
    - no
    - Asymmetric information sending is not done in baselibs.
  * - CO_01_06
    - Information from a sender received by only a subset of the receivers
    - no
    - This is not done in baselibs.
  * - CO_01_07
    - Blocking access to a communication channel
    - no
    - There are no communication channels in baselibs.

#### Shared information inputs

Same information input used by multiple functions.

.. list-table:: DFA shared information inputs
  :header-rows: 1
  :widths: 10,20,10,20

  * - ID
    - Violation cause shared information inputs
    - Applicability
    - Rationale
  * - SI_01_02
    - Configuration data
    - no
    - There is no shared config data in baselibs.
  * - SI_01_03
    - Constants, or variables, being global to the two software functions
    - no
    - No global variables are used in baselibs.
  * - SI_01_04
    - Basic software passes data (read from hardware register and converted into logical information) to two applications software functions
    - no
    - No shared low level data are used between baselibs.
  * - SI_01_05
    - Data / function parameter arguments / messages delivered by software function to more than one other function
    - no
    - No common input can be seen in architecture of baselibs.

#### Unintended impact

Unintended impacts to function due to various failures.

.. list-table:: DFA unintended impact
  :header-rows: 1
  :widths: 10,20,10,20

  * - ID
    - Violation cause unintended impact
    - Applicability
    - Rationale
  * - UI_01_01
    - Memory miss-allocation and leaks
    - no
    - Not a specific baselibs topic, therefore covered at platform DFA.
  * - UI_01_02
    - Read/Write access to memory allocated to another software element
    - yes
    - As baselibs are in context of a application, they may access their memory, [[FEAT_SAF_DFA__BASELIBS__MEMORY_ACCESS]]
  * - UI_01_03
    - Stack/Buffer under-/overflow
    - no
    - Not a specific baselibs topic, therefore covered at platform DFA.
  * - UI_01_04
    - Deadlocks
    - yes
    - shared memory or file access may lead to deadlock, [[FEAT_SAF_DFA__BASELIBS__LOCKED_RESSOURCE]]
  * - UI_01_05
    - Livelocks
    - no
    - Should be covered together with deadlock.
  * - UI_01_06
    - Blocking of execution
    - yes
    - As baselibs are in context of a application, they may block execution, [[FEAT_SAF_DFA__BASELIBS__BLOCKED_EXECUTION]]
  * - UI_01_07
    - Incorrect allocation of execution time
    - no
    - Execution time allocated by (external) OS on platform level, should be covered centrally at platform level.
  * - UI_01_08
    - Incorrect execution flow
    - no
    - Execution flow controlled by (external) OS on platform level, should be covered centrally at platform level.
  * - UI_01_09
    - Incorrect synchronization between software elements
    - no
    - There is no need for synchronization for baselibs.
  * - UI_01_10
    - CPU time depletion
    - yes
    - Baselibs may deplete or suffer from depletion, [[FEAT_SAF_DFA__BASELIBS__CPU_STARVATION]]
  * - UI_01_11
    - Memory depletion
    - no
    - Not a specific baselibs topic, therefore covered at platform DFA.
  * - UI_01_12
    - Other HW unavailability
    - no
    - No special HW used for baselibs.

# DFA

For all identified applicable failure initiators, the DFA is performed in the following section.

### memory access

{{artifact:FEAT_SAF_DFA__BASELIBS__MEMORY_ACCESS:status,safety-level,security}}

### locked ressource

{{artifact:FEAT_SAF_DFA__BASELIBS__LOCKED_RESSOURCE:status,safety-level,security}}

### concurrent file access

{{artifact:FEAT_SAF_DFA__BASELIBS__CONC_FILE_ACCESS:status,safety-level,security}}

### concurrent memory access

{{artifact:FEAT_SAF_DFA__BASELIBS__CONC_MEMORY_ACCESS:status,safety-level,security}}

### blocked execution

{{artifact:FEAT_SAF_DFA__BASELIBS__BLOCKED_EXECUTION:status,safety-level,security}}

### CPU starvation

{{artifact:FEAT_SAF_DFA__BASELIBS__CPU_STARVATION:status,safety-level,security}}

