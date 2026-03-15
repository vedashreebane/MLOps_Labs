# Lab 5: Terraform on GCP

## What is Terraform?
Terraform is a tool that lets you create and manage cloud infrastructure using code. Instead of clicking around in the GCP Console, you write a file describing what you want and Terraform builds it for you.

## What I did in this lab

### Part 1: Setup
- Installed Terraform and configured GCP credentials using a service account key
- Created `main.tf` with the Google Cloud provider pointing to my GCP project
- Ran `terraform init` to download the GCP plugin

### Part 2: Created a VM
- Wrote a `google_compute_instance` resource block in `main.tf`
- Ran `terraform plan` to preview the changes
- Ran `terraform apply` to create an `f1-micro` VM called `terraform-vm` in `us-central1-a`

### Part 3: Modified the VM
- Changed the machine type from `f1-micro` to `e2-micro`
- Added labels: `environment: development` and `owner: team-terraform`
- Increased boot disk size to 12GB
- Added `allow_stopping_for_update = true` to allow Terraform to stop and restart the VM during updates
- Ran `terraform apply` to apply the changes

### Part 4: Added a Storage Bucket
- Added a `google_storage_bucket` resource block to `main.tf`
- Bucket name: `terraform-lab-bucket-unique-12345`, location: `us-central1`
- Ran `terraform apply` to create the bucket

### Part 5: Destroyed Resources
- Ran `terraform destroy` to delete both the VM and the storage bucket
- Verified in GCP Console that all resources were removed

### Part 6: Terraform Files
- `terraform.tfstate` — auto-generated file Terraform uses to track what it has built. Never manually edited.
- `.terraform/` — created by `terraform init`, contains the downloaded GCP provider plugin
- `.terraform.lock.hcl` — records the exact provider version used so the setup is reproducible

## Files

| File | Description |
|------|-------------|
| `main.tf` | Main Terraform configuration file with all resource definitions |
| `.terraform.lock.hcl` | Provider version lock file |
| `terraform show.txt` | Output of `terraform show` showing the full state of resources |
| `vm_instance.png` | Screenshot of the VM in GCP Console showing e2-micro, labels, and disk size |
| `gcs_bucket.png` | Screenshot of the storage bucket in GCP Console |

## Commands Used

```bash
terraform init      # Download GCP provider plugin
terraform plan      # Preview changes before applying
terraform apply     # Create or update infrastructure
terraform show      # View current state of all resources
terraform destroy   # Delete all resources
```
