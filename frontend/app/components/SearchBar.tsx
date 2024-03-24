import { useState } from "react";
import { useRouter } from "next/navigation";

function SearchBar() {
  const [searchQuery, setSearchQuery] = useState("");
  const router = useRouter();

<<<<<<< HEAD
  const buttonStyle = {
  color: 'white',
  backgroundColor: 'blue',
  padding: '10px',
  borderRadius: '5px',
  };

=======
>>>>>>> main
  const handleSearch = (e: any) => {
    e.preventDefault();
    router.push(`/search/searchQ=${searchQuery}`);
  };

<<<<<<< HEAD
  const filterHandler = (e: any) => {
    e.preventDefault(); // Prevent default link behavior
    router.push(`/filter/${searchQuery}`); // Construct the filter URL
  }

=======
>>>>>>> main
  return (
    <form onSubmit={handleSearch}>
      <input
        type="text"
        placeholder="Search..."
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
      />
      <button type="submit">Search</button>
<<<<<<< HEAD
      <button         
        className="btn btn-light fw-bold border-white bg-white"
        type="button"
        name="action"
        value="filter"
        style={buttonStyle}
        onClick={filterHandler}
      >
      Filter
      </button>
=======
>>>>>>> main
    </form>
  );
}

export default SearchBar;
