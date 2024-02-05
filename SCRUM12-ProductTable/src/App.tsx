import { MantineProvider } from "@mantine/core";
import TableComp, { User } from "./Table";

function App() {
  return (
    <MantineProvider>
      <div>
        <TableComp />
      </div>
    </MantineProvider>
  );
}

export default App;
