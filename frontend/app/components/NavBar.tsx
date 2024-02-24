export function NavBar() {
  return (
    <nav style={{ display: "flex" }}>
      <div className="text-white">
        <a href="#">Home</a>
        <a href="#" style={{ textDecoration: "none" }}>
          Pages
        </a>
        <a href="#" style={{ textDecoration: "none" }}>
          Discussion Board{" "}
        </a>
        <a href="/table" style={{ textDecoration: "none" }}>
          Compare
        </a>
      </div>
      <div style={{ marginLeft: "auto", display: "flex" }}>
        <p>Welcome,</p>
        <a
          style={{ margin: 0, marginLeft: 5, textDecoration: "none" }}
          href="{% url 'logout' %}"
        >
          Logout
        </a>
      </div>
      <div style={{ marginLeft: "auto" }}>
        <a href="/login" style={{ textDecoration: "none" }}>
          Login/Signup
        </a>
      </div>
    </nav>
  );
}
