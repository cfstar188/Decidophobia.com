import { useState } from "react";
import { useRouter } from "next/navigation";
import Button from '@mui/material/Button';

function SearchBar() {
  const [searchQuery, setSearchQuery] = useState("");
  const router = useRouter();

  const handleSearch = (e: any) => {
    e.preventDefault();
    router.push(`/search/searchQ=${searchQuery}`);
  };

  return (
    <form className="homeForm"  onSubmit={handleSearch}>
      <input style={{color: 'black', width : '50%', height : "100%", padding: "10px", borderRadius: "5px", border: "1px solid #ccc"}}
        type="text"
        placeholder="Search..."
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
      />
      <Button variant="contained" type="submit" style={{marginLeft: "10px", backgroundColor:'#2E8BC0'}}>Search</Button>
    </form>
  );
}

export default SearchBar;
