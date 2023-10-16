import Image from 'next/image'
import Link from 'next/link';
import styles from './page.module.css'
import Forms from '../../components/Forms'

export default function Home() {
  return (
    <>
    <Link href="/about/">
    </Link>
    <Forms/>
    </>
  )
}
