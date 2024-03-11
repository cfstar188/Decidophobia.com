import Link from 'next/link';
import { useAtom } from 'jotai';
import { authAtom } from "@/Library/AuthAtom";
// import AuthContext from "@/app/contexts/AuthContext";

export function NavBar() {
  const [auth, setAuth] = useAtom(authAtom);

  const logout = () => {
    setAuth({ isAuthenticated: false, username: '' });
    localStorage.removeItem('token');
  };

  return (
    <nav style={{ display: "flex" }}>
      <div>
        <Link href="/">Home</Link>
        <Link href="#">Discussion Board</Link>
        {auth.isAuthenticated && <Link href="/cart">Shopping Cart</Link>}
      </div>
      {!auth.isAuthenticated ? (
        <div style={{ marginLeft: "auto", display: "flex" }}>
          <p>Welcome, {auth.username}!</p>
          <Link href="/logout" onClick={logout}>Logout</Link>
        </div>
      ) : (
        <div style={{ marginLeft: "auto" }}>
          <Link href="/login">Login/Signup</Link>
        </div>
      )}
    </nav>
  );
}
