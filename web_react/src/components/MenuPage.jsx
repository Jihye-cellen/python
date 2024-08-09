import React from 'react'
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Container from 'react-bootstrap/Container';
import RouterPage from './RouterPage';
import { useLocation } from 'react-router-dom';

const MenuPage = () => {
  const { pathname } = useLocation()
  const onLogout = (e)=>{
    e.preventDefault();
    if(!window.confirm('로그아웃을 하시겠습니까?')) return;
    sessionStorage.clear()
    navigator('/')
  }


  return (
    <>
      <Navbar bg="primary" data-bs-theme="dark">
        <Container>
          <Navbar.Brand href="/">Home</Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link href="/shop/search" className={pathname === '/shop/search' && 'active'}>
              상품검색
            </Nav.Link>
            <Nav.Link href="/shop" className={pathname === '/shop' && 'active'}>
              상품목록
            </Nav.Link>
          </Nav>
          <Nav>
            {sessionStorage.getItem('email') ?
              <>
                <Nav.Link href="/mypage" className='active'>
                  {sessionStorage.getItem("email")}님
                </Nav.Link>
                <Nav.Link>
                  로그아웃
                </Nav.Link>
              </>
              :
              <Nav.Link href="/login" className={pathname === '/login' && 'active'}>
                로그인
              </Nav.Link>
            }
          </Nav>
        </Container>
      </Navbar>
      <RouterPage />
    </>
  )
}

export default MenuPage