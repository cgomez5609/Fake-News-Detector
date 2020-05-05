import tools
from pathlib import Path
import pandas as pd

def main(file_to_be_sampled, output_directory, output_filename, sample_fraction):
    
    filename = file_to_be_sampled
    file_path = Path(__file__).parent.parent.parent / "data" / "raw" / filename
    
    if file_path.exists():
        df = pd.read_csv(file_path)
        
        fraction = sample_fraction
        df_sample = tools.get_dataframe_sample(df, fraction=fraction)
        
        df_sample["label"] = "true"
        
        output_dir = output_directory
        
        output_path = Path(__file__).parent.parent.parent / "data" / output_dir
        
        output_filename = output_filename
        
        print(output_filename)
        
        if output_path.exists():
            print("Path exists")
            print(output_path)
            final_output = output_path / output_filename
            df_sample.to_csv(final_output, sep="\t", index=False)
        else:
            print("Path doesn't exist. One is was created at:")
            print(output_path)
            output_path.mkdir(parents=True, exist_ok=True)
            final_output = output_path / output_filename
            df_sample.to_csv(final_output, sep="\t", index=False)
            
    else:
        print(file_path)
        print("Not a valid path")
    
if __name__ == "__main__":
    # execute only if run as a script
    #main("True.csv", "samples", "true_35.tsv", 0.35)
    
    # output_path = Path().absolute() / "data" / "samples" / "True_Fake_35.tsv"
    
    # path_fake = Path().absolute() / "data" / "samples" / "Fake_35.tsv"
    # path_true = Path().absolute() / "data" / "samples" / "True_35.tsv"
    
    # df_fake = pd.read_csv(path_fake, sep="\t")
    # df_true = pd.read_csv(path_true, sep="\t")
    
    # df_combined = pd.concat([df_fake, df_true])
    
    # df_combined.to_csv(output_path, sep="\t", index=False)
    
    
    