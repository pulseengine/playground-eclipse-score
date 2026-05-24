---
id: DOC-ASPICE-94310
title: Aspice
type: specification
status: approved
tags: [eclipse-score]
---

.. _standard_aspice_pam4:

# ASPICE 4.0

This incorporates the detailed description of the `Automotive SPICE PAM
v4.0 <https://vda-qmc.de/wp-content/uploads/2023/12/Automotive-SPICE-PAM-v40.pdf>`__
to support the performance of process assessments, so that the process
assessment model can be used for its intended purpose.

`Automotive SPICE PAM
v4.0 <https://vda-qmc.de/wp-content/uploads/2023/12/Automotive-SPICE-PAM-v40.pdf>`__
provides following copyright release statement:

You may not alter, transform, or build upon this work without the prior consent of the VDA Quality Management Center. Such consent may be given provided ISO copyright is not infringed.

The detailed descriptions contained in this document may be incorporated as part of any tool or other material to support the performance of process assessments, so that this process assessment model can be used for its intended purpose, provided that any such material is not offered for sale.

All distribution of derivative works shall be made at no cost to the recipient.

## Copyright notice

There is no alteration, transformation or building upon in this project. Detailed descriptions are included to facilitate process assessment in projects and are provided in an open source framework free of charge.

## Tailoring

| Standard's requirements in this document are already tailored to the SW platform project:
|
| - Generally, requirements (base (BP) and generic practices (GP)) and work product (information item characteristics (IIC)) links are only included if those are relevant (i.e., not tailored out).
|
| - Included are only the following process groups and the listed processes:
|   - SWE: Software Engineering Process Group (SWE.1-SWE.6)
|   - MAN: Management Process Group (MAN.3, MAN.5)
|   - SUP: Supporting Process Group (SUP.1, SUP.8-SUP.10)
|   - SPL: Supply Process Group (SPL.2)
|   - REU: Reuse Process Group (REU.2)
|   - PIM: Process Improvement Process Group (PIM.3)
|
| - Excluded are also the following process groups or processes from the mentioned process groups above:
|   - SYS: System Engineering Process Group (pure SW development project)
|   - HWE: Hardware Engineering Process Group (pure SW development project)
|   - MLE: Machine Learning Engineering Process Group (not applicable for now)
|   - SUP: SUP.11 - Machine Learning Data Management (not applicable for now)
|   - MAN: MAN.6 - Measurements (not applicable for now)
|   - VAL: Validation process group (pure SW with no (automobile) user interaction)
|   - ACQ: Acquisition process group (because there is no contracted supplier of the project)
|   - Process capability level 4 and 5 (GP4 and GP5)

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   man/index
   swe/index
   mle/index
   sup/index
   spl/index
   reu/index
   pim/index
   iic/index

## PA 2.1 Process performance management process attribute

The performance management process attribute is a measure of the extent
to which the performance of the process is managed.

### Process attribute achievements

1. Strategy for the performance of the process is defined based on identified objectives.
2. Performance of the process is planned.
3. Performance of the process is monitored and adjusted to meet the planning.
4. Needs for human resources including responsibilities and authorities for performing the process are determined.
5. Needs for physical and material resources are determined.
6. Persons performing the process are prepared for executing their responsibilities.
7. Physical and material resources for performing the process are identified, made available, allocated and used.
8. Interfaces between the involved parties are managed to ensure both effective communication and the assignment of responsibilities.

### Generic practices

### GP2.1.1: Identify the objectives and define a strategy for the performance of the process.

{{artifact:STD_REQ__ASPICE_40__GP-211:status,safety-level,security}}}}

### GP2.1.2: Plan the performance of the process.

{{artifact:STD_REQ__ASPICE_40__GP-212:status,safety-level,security}}}}

### GP2.1.3: Determine resource needs.

{{artifact:STD_REQ__ASPICE_40__GP-213:status,safety-level,security}}}}

### GP2.1.4: Identify and make available resources.

{{artifact:STD_REQ__ASPICE_40__GP-214:status,safety-level,security}}}}

### GP2.1.5: Monitor and adjust the performance of the process.

{{artifact:STD_REQ__ASPICE_40__GP-215:status,safety-level,security}}}}

### GP2.1.6: Manage the interfaces between involved parties.

{{artifact:STD_REQ__ASPICE_40__GP-216:status,safety-level,security}}}}

## PA 2.2 Work product management process attribute

The work product management process attribute is a measure of the extent
to which the work products produced by the process are appropriately managed.

### Process attribute achievements

1. Requirements for the work products of the process are defined.
2. Requirements for storage and control of the work products are defined.
3. The work products are appropriately identified, stored, and controlled.
4. The work products are reviewed and adjusted as necessary to meet requirements.

### Generic practices

### GP2.2.1: Define the requirements for the work products.

{{artifact:STD_REQ__ASPICE_40__GP-221:status,safety-level,security}}}}

### GP2.2.2: Define the requirements for storage and control of the work products.

{{artifact:STD_REQ__ASPICE_40__GP-222:status,safety-level,security}}}}

### GP2.2.3: Identify, store and control the work products.

{{artifact:STD_REQ__ASPICE_40__GP-223:status,safety-level,security}}}}

### GP2.2.4: Review and adjust work products.

{{artifact:STD_REQ__ASPICE_40__GP-224:status,safety-level,security}}}}

## PA 3.1 Process definition process attribute

The process definition process attribute is a measure of the extent to
which a standard process is maintained to support the deployment of the defined process.

### Process attribute achievements

1. A standard process is developed, established, and maintained that describes the fundamental elements that must be incorporated into a defined process.
2. The required inputs and the expected outputs for the standard process are defined.
3. Roles, responsibilities, authorities, and required competencies for performing the standard process are defined.
4. Tailoring guidelines for deriving the defined process from the standard process are defined.
5. Required physical and material resources and process infrastructure needs are determined as part of the standard process.
6. Suitable methods and required activities for monitoring the effectiveness, suitability and adequacy of the process are determined.

### Generic practices

### GP3.1.1: Establish and maintain the standard process.

{{artifact:STD_REQ__ASPICE_40__GP-311:status,safety-level,security}}}}

### GP3.1.2: Determine the required competencies.

{{artifact:STD_REQ__ASPICE_40__GP-312:status,safety-level,security}}}}

### GP3.1.3: Determine the required resources.

{{artifact:STD_REQ__ASPICE_40__GP-313:status,safety-level,security}}}}

### GP3.1.4: Determine suitable methods to monitor the standard process.

{{artifact:STD_REQ__ASPICE_40__GP-314:status,safety-level,security}}}}

## PA 3.2 Process deployment process attribute

The process deployment process attribute is a measure of the extent to which
the standard process is deployed as a defined process to achieve its process outcomes.

### Process attribute achievements

1. A defined process is deployed based upon an appropriately selected and/or tailored standard process.
2. Assignment of persons necessary for performing the defined process to roles is performed and communicated.
3. Required education, training and experience is ensured and monitored for the person(s) assigned to the roles.
4. Required resources for performing the defined process are made available, allocated, and maintained.
5. Appropriate information is collected and analyzed as a basis for understanding the behavior of the process.

### Generic practices

### GP3.2.1: Deploy a defined process that satisfies the context specific requirements of the use of the standard process.

{{artifact:STD_REQ__ASPICE_40__GP-321:status,safety-level,security}}}}

### GP3.2.2: Ensure required competencies for the defined roles.

{{artifact:STD_REQ__ASPICE_40__GP-322:status,safety-level,security}}}}

### GP3.2.3: Ensure required resources to support the performance of the defined process.

{{artifact:STD_REQ__ASPICE_40__GP-323:status,safety-level,security}}}}

### GP3.2.4: Monitor the performance of the defined process.

{{artifact:STD_REQ__ASPICE_40__GP-324:status,safety-level,security}}}}

## Appendix


