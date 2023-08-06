import pydactim as pyd
import os

@pyd.timed
def preproc(sub_path, model_path, ses="ses-01", ref="T1w", normalize=False, keep_all=True):
    # Sub of the patient bids number
    # Path of the reference sequence
    
    # Checking errors
    sub = os.path.basename(sub_path)
    if "sub" not in sub:
        raise ValueError("ERROR - Could not find a sub number in the data_path, make sure it is bids compliant")

    ses_path = os.path.join(sub_path, ses)
    if not os.path.isdir(ses_path):
        raise ValueError(f"ERROR - Could not find a directory with the following session number {ses}")

    modalities = os.listdir(ses_path)
    if "anat" not in modalities:
        raise ValueError("ERROR - Can not start process without the anat directory")
    
    anat_paths = os.listdir(os.path.join(ses_path, "anat"))
    ref_path = f"{sub}_{ses}_{ref}.nii.gz"
    if ref_path not in anat_paths:
        raise FileNotFoundError(f"ERROR - The following reference filename could not be found:\n\t{ref_path}")
    
    # Starting to preproc the reference sequence
    print(f"INFO - Starting preprocessing for the reference image at\n\t{ref_path}")
    ref_brain, ref_brain_mask, ref_crop = ref_preproc(ref_path, normalize)

    # Starting to loop through each sequence
    print(f"INFO - Starting preprocessing for the following modalities:\n\t{','.join(modalities)}")
    print("INFO - Starting with anatomic sequences")
    for seq in anat_paths:
        seq_path = os.path.join(anat_paths, seq)
        # Check if the file is a nii.gz
        if seq_path.endswith("nii.gz") and seq_path != ref_path and pyd.is_native(seq_path):
            print("INFO - Nifti file found: {seq_path}")
            # Starting preproc for the current sequence path
            seq_path = other_preproc(seq_path, ref_brain, ref_crop, normalize)

    print("INFO - Continuing with diffusion sequences")
    dwi_paths = os.listdir(os.path.join(ses_path, "dwi"))
    for seq in dwi_paths:
        seq_path = os.path.join(dwi_paths, seq)
        # Check if the file is a nii.gz
        if seq_path.endswith("nii.gz") and seq_path != ref_path and pyd.is_native(seq_path) and pyd.is_useful(seq_path):
            print("INFO - Nifti file found: {seq_path}")
            # Starting preproc for the current sequence path
            seq_path = other_preproc(seq_path, ref_brain, ref_brain_mask, ref_crop, normalize)

    print("INFO - Continuing with perfusion sequences")
    perf_paths = os.listdir(os.path.join(ses_path, "perf"))
    for seq in perf_paths:
        seq_path = os.path.join(perf_paths, seq)
        # Check if the file is a nii.gz
        if seq_path.endswith("nii.gz") and seq_path != ref_path and pyd.is_native(seq_path) and pyd.is_useful(seq_path):
            print("INFO - Nifti file found: {seq_path}")
            # Starting preproc for the current sequence path
            seq_path = other_preproc(seq_path, ref_brain, ref_brain_mask, ref_crop, normalize)

@pyd.timed
def ref_preproc(ref_path, normalize, model_path):
    # crop => resample => n4 bias field correction => skull stripping => crop
    ref_path_cropped, crop_idx_1 = pyd.crop(ref_path)
    ref_path_resampled = pyd.resample(ref_path_cropped, 1)[0]
    ref_path_corrected = pyd.n4_bias_field_correction(ref_path_resampled, mask=True)
    ref_path_brain, ref_path_brain_mask = pyd.skull_stripping(ref_path_corrected, model_path, mask=True)
    ref_path_brain_cropped, crop_idx_2 = pyd.crop(ref_path_brain)
    ref_path_brain_mask_cropped = pyd.apply_crop(ref_path_brain_mask, crop_idx_2)
    if normalize: ref_path_final = pyd.normalize(ref_path_brain_cropped)
    else: ref_path_final = ref_path_brain_cropped
    return ref_path_final, ref_path_brain_mask, crop_idx_2

@pyd.timed
def other_preproc(seq_path, ref_brain, ref_brain_mask, ref_crop, normalize):
    # registration => apply brain mask => apply crop => n4 bias field correction
    seq_path_registered = pyd.registration(ref_brain, seq_path)
    seq_path_brain = pyd.apply_mask(seq_path_registered, ref_brain_mask, suffix="brain")
    seq_path_cropped = pyd.apply_crop(seq_path_brain, crop=ref_crop)
    seq_path_corrected = pyd.n4_bias_field_correction(seq_path_cropped, mask=True)
    if normalize: seq_path_normalized = pyd.normalize(seq_path_corrected)

if __name__ == "__main__":
    preproc(
        data_path="",
        model_path="",
        ses="ses-01",
        ref="T1w", 
        normalize=False, 
        keep_all=True
    )