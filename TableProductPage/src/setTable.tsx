import { CloseButton } from "@mantine/core";

export function CloseButtonCus({ id, setData }: any) {
  return <CloseButton onClick={() => setData(id)} />;
}
